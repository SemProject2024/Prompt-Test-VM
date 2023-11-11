const aboutButton = document.getElementById('about');
aboutButton.addEventListener('click', function() {
window.location.href = 'about.html';
        });

const newChatButton = document.getElementById('newChatButton');
newChatButton.addEventListener('click', function() {
            window.location.href = 'chat.html'; 
        });

const credentials = document.getElementById('credentials');
credentials.addEventListener('click', function() {
            window.location.href = 'credentials.html'; 
        });
const provisionedResources = document.getElementById('provisionedResources');
provisionedResources.addEventListener('click', function() {
            window.location.href = 'provisioned-resources.html'; 
        });

const signOut = document.getElementById('signOut');
signOut.addEventListener('click', function() {
            window.location.href = 'login.html'; 
        });



const profile = document.getElementById('profile');
profile.addEventListener('click', function() {
            window.location.href = 'profile.html'; 
        });

