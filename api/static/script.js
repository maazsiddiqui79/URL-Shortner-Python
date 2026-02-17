document.addEventListener('DOMContentLoaded', () => {
    const themeToggleBtn = document.getElementById('theme-toggle');
    const body = document.body;
    const icon = themeToggleBtn.querySelector('i');

    // Check for saved user preference, if any, on load
    const currentTheme = localStorage.getItem('theme');
    if (currentTheme) {
        body.setAttribute('data-theme', currentTheme);
        updateIcon(currentTheme);
    }

    themeToggleBtn.addEventListener('click', () => {
        let theme = body.getAttribute('data-theme');
        if (theme === 'dark') {
            body.setAttribute('data-theme', 'light');
            localStorage.setItem('theme', 'light');
            updateIcon('light');
        } else {
            body.setAttribute('data-theme', 'dark');
            localStorage.setItem('theme', 'dark');
            updateIcon('dark');
        }
    });

    function updateIcon(theme) {
        // Assuming we use FontAwesome or similar simple text icons
        if (theme === 'dark') {
            themeToggleBtn.innerHTML = '☀️'; // Sun icon for light mode switch
            themeToggleBtn.title = "Switch to Light Mode";
        } else {
            themeToggleBtn.innerHTML = '🌙'; // Moon icon for dark mode switch
            themeToggleBtn.title = "Switch to Dark Mode";
        }
    }
    
    // Auto-dismiss alerts after 5 seconds
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        setTimeout(() => {
            alert.style.opacity = '0';
            setTimeout(() => alert.remove(), 500); // Wait for fade out
        }, 5000);
    });
});
