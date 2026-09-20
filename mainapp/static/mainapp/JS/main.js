document.addEventListener('DOMContentLoaded', () => {
    
    // -------------------------------------------------------------
    // 1. GESTION DU FORMULAIRE DE CONTACT (AJAX)
    // -------------------------------------------------------------
    const contactForm = document.getElementById('contact-form');
    const responseDiv = document.getElementById('form-response');

    if (contactForm) {
        contactForm.addEventListener('submit', async (e) => {
            e.preventDefault();

            // Interception du bouton et état de chargement
            const submitBtn = contactForm.querySelector('button[type="submit"]');
            const originalBtnText = submitBtn.innerHTML;

            submitBtn.disabled = true;
            submitBtn.innerHTML = `ENVOI EN COURS... <span class="spinner-border spinner-border-sm ms-2" role="status"></span>`;
            
            // Reinitialisation des messages
            if (responseDiv) {
                responseDiv.className = '';
                responseDiv.textContent = '';
            }

            const formData = new FormData(contactForm);

            try {
                // Récupération du token CSRF
                const csrfToken = formData.get('csrfmiddlewaretoken');

                const response = await fetch(contactForm.action, {
                    method: 'POST',
                    body: formData,
                    headers: {
                        'X-Requested-With': 'XMLHttpRequest',
                        'X-CSRFToken': csrfToken
                    }
                });

                const data = await response.json();

                if (responseDiv) {
                    if (response.ok) {
                        responseDiv.className = 'alert alert-dark border-2 border-dark rounded-0 mt-3 fw-bold';
                        responseDiv.textContent = data.message || "Message envoyé avec succès !";
                        contactForm.reset();
                    } else {
                        responseDiv.className = 'alert alert-danger border-2 border-dark rounded-0 mt-3 fw-bold';
                        responseDiv.textContent = data.message || "Erreur lors de la validation du formulaire.";
                    }
                }
            } catch (error) {
                console.error("Erreur Fetch:", error);
                if (responseDiv) {
                    responseDiv.className = 'alert alert-danger border-2 border-dark rounded-0 mt-3 fw-bold';
                    responseDiv.textContent = "Une erreur est survenue lors de l'envoi. Vérifiez votre connexion.";
                }
            } finally {
                // Réactivation du bouton d'envoi
                submitBtn.disabled = false;
                submitBtn.innerHTML = originalBtnText;
            }
        });
    }

    // -------------------------------------------------------------
    // 2. COPIE DE L'EMAIL DANS LE PRESSE-PAPIER
    // -------------------------------------------------------------
    const copyBtn = document.getElementById('copy-email-btn');
    
    if (copyBtn) {
        copyBtn.addEventListener('click', async () => {
            const emailText = 'ndaomoussa07@gmail.com';
            
            try {
                // Utilisation de l'API moderne ou du fallback classique
                if (navigator.clipboard && window.isSecureContext) {
                    await navigator.clipboard.writeText(emailText);
                } else {
                    const textArea = document.createElement('textarea');
                    textArea.value = emailText;
                    document.body.appendChild(textArea);
                    textArea.select();
                    document.execCommand('copy');
                    document.body.removeChild(textArea);
                }
                
                // Feedback visuel sur le bouton
                const originalHTML = copyBtn.innerHTML;
                copyBtn.innerHTML = `<i class="bi bi-check-lg me-1"></i> Copié !`;
                copyBtn.classList.remove('btn-outline-dark');
                copyBtn.classList.add('btn-dark');

                setTimeout(() => {
                    copyBtn.innerHTML = originalHTML;
                    copyBtn.classList.remove('btn-dark');
                    copyBtn.classList.add('btn-outline-dark');
                }, 2000);

            } catch (err) {
                console.error('Erreur lors de la copie :', err);
            }
        });
    }

});