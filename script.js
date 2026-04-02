
document.addEventListener('DOMContentLoaded', () => {
    // === 1. 네비게이션 및 페이지 이동 제어 ===
    const navLinks = document.querySelectorAll('.nav-link, .nav-link-btn');
    const pages = document.querySelectorAll('.page');
    const bottomNavItems = document.querySelectorAll('.bottom-nav .nav-item');

    function navigateTo(targetId) {
        pages.forEach(p => p.classList.remove('active'));
        const targetPage = document.getElementById(targetId);
        if(targetPage) {
            targetPage.classList.add('active');
        } else {
            document.getElementById('page-home').classList.add('active');
        }

        bottomNavItems.forEach(item => {
            if(item.dataset.target === targetId) item.classList.add('active');
            else item.classList.remove('active');
        });

        closeSidebar();
    }

    navLinks.forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            const targetId = link.dataset.target;
            // li elements might need stopPropagation if layered, 
            // but here it's fine.
            navigateTo(targetId);
        });
    });

    document.getElementById('logoHome').addEventListener('click', () => {
        navigateTo('page-home');
    });

    // === 2. 사이드바 제어 ===
    const menuBtn = document.getElementById('menuToggle');
    const closeBtn = document.getElementById('menuClose');
    const sidebar = document.getElementById('sidebar');
    const overlay = document.getElementById('sidebarOverlay');

    function openSidebar() {
        sidebar.classList.add('open');
        overlay.classList.add('active');
    }
    function closeSidebar() {
        sidebar.classList.remove('open');
        overlay.classList.remove('active');
    }

    menuBtn.addEventListener('click', openSidebar);
    closeBtn.addEventListener('click', closeSidebar);
    overlay.addEventListener('click', closeSidebar);

    // === 3. 사이드바 아코디언 제어 ===
    const accordions = document.querySelectorAll('.accordion-header');
    accordions.forEach(acc => {
        acc.addEventListener('click', () => {
            // 다른 아코디언은 닫기(선택사항)
            // document.querySelectorAll('.accordion-content').forEach(c => c.classList.remove('active'));
            // document.querySelectorAll('.accordion-header i').forEach(icon => icon.className = 'fa-solid fa-chevron-down');
            
            const content = acc.nextElementSibling;
            const icon = acc.querySelector('i');
            
            if(content.classList.contains('active')) {
                content.classList.remove('active');
                icon.className = 'fa-solid fa-chevron-down';
            } else {
                content.classList.add('active');
                icon.className = 'fa-solid fa-chevron-up';
            }
        });
    });
});
    