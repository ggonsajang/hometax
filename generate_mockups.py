import os

menus = [
    {"main": "세금신고", "subs": ["신고서 조회/삭제/부속서류", "부가가치세 신고", "종합소득세 신고", "양도소득세 신고"]},
    {"main": "납부ㆍ고지ㆍ환급", "subs": ["세금납부", "납부내역 조회", "국세환급", "국세고지"]},
    {"main": "국세증명ㆍ사업자등록", "subs": ["즉시발급 증명", "사실확인 후 발급 증명", "기타 민원 증명", "사업자등록 신청"]},
    {"main": "지급명세서ㆍ자료제출", "subs": ["일용/간이지급명세서 제출", "근로사업 등 지급명세서 제출", "과세자료 제출"]},
    {"main": "장려금ㆍ연말정산", "subs": ["근로/자녀장려금 정기 신청", "연말정산간소화", "전자기부금영수증"]},
    {"main": "세금계산서ㆍ현금영수증", "subs": ["전자(세금)계산서 발급", "현금영수증(근로자)", "현금영수증(사업자)"]},
    {"main": "상담ㆍ불복ㆍ고충", "subs": ["상담하기", "탈세 제보"]},
    {"main": "세무대리ㆍ납세관리", "subs": ["세무대리 공통 조회", "수임 납세자 관리"]},
    {"main": "비회원", "subs": ["근로ㆍ자녀장려금(정기) 조회", "민원증명 발급"]},
    {"main": "My홈택스(개인)", "subs": ["모범납세자 내역", "나의 세무담당"]},
    {"main": "My홈택스(사업자)", "subs": ["고지서 송달장소 안내", "과세자료 제출내역"]},
    {"main": "인증센터", "subs": ["공인인증서 안내", "지문인증센터"]},
    {"main": "나의 정보", "subs": ["회원 정보 수정", "비밀번호 변경"]},
    {"main": "고객센터", "subs": ["공지사항", "이용시간안내"]},
    {"main": "설정", "subs": ["설정"]}
]

def generate_mock_page_content(idx, sub_idx, main_title, sub_title):
    page_id = f"page-gen-{idx}-{sub_idx}"
    content = ""
    
    # 세금신고 그룹
    if "조회/삭제/부속서류" in sub_title:
        content = """
            <div class="card bg-blue text-white" style="text-align:center;">
                <h3>최근 제출된 신고서 (조회)</h3>
                <h2 style="margin:10px 0;">2건</h2>
            </div>
            <div class="card">
                <div style="font-size:0.9rem; color:#666; margin-bottom:5px;">2026.01.20 | 부가가치세 신고</div>
                <div style="display:flex; justify-content:space-between; align-items:center;">
                    <span style="font-weight:bold; font-size:1.1rem;">접수완료</span>
                    <div>
                        <button class="btn-sm bg-gray">삭제</button>
                        <button class="btn-sm bg-blue text-white">부속서류</button>
                    </div>
                </div>
            </div>
        """
    elif "부가가치세 신고" in sub_title:
        content = """
            <div class="card bg-gradient text-white">
                <h2>부가가치세 정기신고</h2>
                <p>일반과세자 / 간이과세자 정기신고기한 내 신고</p>
                <button class="btn-primary" style="margin-top:15px; background:white; color:#005bb8;">정기신고 작성</button>
            </div>
            <div class="card">
                <h3>기타 신고</h3>
                <ul style="list-style:none; margin-top:10px;">
                    <li style="padding:10px 0; border-bottom:1px solid #eee;">기한후신고 <i class="fa-solid fa-chevron-right" style="float:right;"></i></li>
                    <li style="padding:10px 0; border-bottom:1px solid #eee;">수정신고 <i class="fa-solid fa-chevron-right" style="float:right;"></i></li>
                    <li style="padding:10px 0;">조기환급신고 <i class="fa-solid fa-chevron-right" style="float:right;"></i></li>
                </ul>
            </div>
        """
    elif "종합소득세 신고" in sub_title:
        content = """
            <div class="card" style="text-align:center;">
                <h3 style="color:#004d99;">종합소득세 도와주기 서비스</h3>
                <p style="color:#666; font-size:0.9rem; margin:10px 0;">모바일로 간편하게 모두채움 신고를 완료하세요!</p>
                <button class="btn-primary" style="margin-top:10px;">모두채움 신고서 확인</button>
            </div>
            <div class="card">
                <p style="font-weight:bold; margin-bottom:10px;">일반 신고 (직접 작성)</p>
                <button class="btn-sm bg-gray" style="width:100%; padding:15px; margin-bottom:10px;">일반신고서 작성</button>
                <button class="btn-sm bg-gray" style="width:100%; padding:15px;">단순경비율신고서 작성</button>
            </div>
        """
    
    # 납부
    elif "세금납부" in sub_title:
        content = """
            <div class="card" style="text-align:center;">
                <p style="color:#666;">납부 예정 세액 (고지분)</p>
                <h1 style="color:#004d99; margin:10px 0;">1,250,000 원</h1>
                <button class="btn-primary" style="margin-top:15px; width:100%;">지금 바로 납부하기</button>
            </div>
        """
    elif "환급" in sub_title:
        content = """
            <div class="card bg-blue text-white" style="text-align:center;">
                <h3>미수령 환급금</h3>
                <h2 style="margin:10px 0;">0 원</h2>
            </div>
            <div class="card">
                <h3 style="margin-bottom:15px;">환급금 수령 계좌 관리</h3>
                <p style="color:#666; margin-bottom:10px;">현재 등록된 계좌: 신한은행 110-***-******</p>
                <button class="btn-sm bg-gray" style="width:100%;">계좌 변경/등록</button>
            </div>
        """

    # 국세증명
    elif "즉시발급 증명" in sub_title:
        content = """
            <div class="card-grid" style="display:grid; grid-template-columns:1fr 1fr; gap:10px;">
                <div class="card" style="text-align:center; padding:20px 10px;">
                    <i class="fa-solid fa-file-invoice" style="font-size:2rem; color:#004d99; margin-bottom:10px;"></i><br><b>소득금액증명</b>
                </div>
                <div class="card" style="text-align:center; padding:20px 10px;">
                    <i class="fa-solid fa-file-signature" style="font-size:2rem; color:#228b22; margin-bottom:10px;"></i><br><b>납세증명서</b>
                </div>
                <div class="card" style="text-align:center; padding:20px 10px;">
                    <i class="fa-solid fa-file-excel" style="font-size:2rem; color:#ffa500; margin-bottom:10px;"></i><br><b>사업자등록증명</b>
                </div>
            </div>
        """
    
    # 사업자등록 신청
    elif "사업자등록 신청" in sub_title:
        content = """
            <div class="card">
                <h3>개인사업자 등록 (개인)</h3>
                <p style="color:#666; font-size:0.9rem; margin:10px 0;">모바일로 간편하게 사업자등록이 가능합니다.</p>
                <button class="btn-primary">신청하기</button>
            </div>
            <div class="card">
                <h3>통신판매업 신고 연계</h3>
                <p style="color:#666; font-size:0.9rem; margin:10px 0;">정부24 연계를 통해 통신판매업 신고도 병행 가능합니다.</p>
                <button class="btn-sm bg-gray" style="width:100%;">정부24 바로가기</button>
            </div>
        """

    # 제출관련
    elif "제출" in sub_title:
        content = """
            <div class="card">
                <h3 style="margin-bottom:15px;">제출 방식 선택</h3>
                <button class="btn-primary" style="margin-bottom:10px; background:#228b22;">엑셀 파일 업로드</button>
                <button class="btn-primary" style="background:#004d99;">직접 화면에서 입력</button>
            </div>
            <div class="card">
                <h3 style="margin-bottom:10px;">최근 제출 내역</h3>
                <p style="color:#666;">(2026.01) 1분기 일용근로소득 지급명세서 - <b style="color:#004d99;">제출완료</b></p>
            </div>
        """

    # 장려금 / 연말정산
    elif "장려금" in sub_title:
        content = """
            <div class="card bg-orange text-white">
                <h2>신청 안내</h2>
                <p style="margin-top:10px;">접수기간 : 2026.05.01 ~ 05.31</p>
            </div>
            <div class="card" style="text-align:center;">
                <p style="margin-bottom:10px;">장려금 산정 예상액 확인 및 신청</p>
                <button class="btn-primary">예상액 조회 및 신청</button>
            </div>
        """
    elif "연말정산간소화" in sub_title:
        content = """
            <div class="card">
                <h3>소득 및 세액 공제 자료 조회</h3>
                <p style="color:#666; font-size:0.9rem; margin-top:5px; margin-bottom:15px;">
                    근로자이신 경우 소득세액공제 자료를 간편하게 제출하고 다운로드 할 수 있습니다.
                </p>
                <button class="btn-primary" style="width:100%; margin-bottom:10px;">건강보험료 조회</button>
                <button class="btn-primary" style="width:100%; margin-bottom:10px;">의료비 조회</button>
                <button class="btn-primary" style="width:100%;">신용카드 등 사용내역 조회</button>
            </div>
            <div class="card">
                <button class="btn-sm bg-blue text-white" style="width:100%; padding:15px;">공제 자료 한번에 PDF 다운로드</button>
            </div>
        """

    # 전자계산서 발급
    elif "계산서 발급" in sub_title:
        content = """
            <div class="card">
                <h3>공급받는 자 정보 (매입자)</h3>
                <input type="text" class="input-field" style="margin-top:10px;" placeholder="사업자등록번호( - 없이)">
                <button class="btn-sm bg-blue text-white" style="width:100%; padding:10px; margin-bottom:10px;">거래처 조회</button>
            </div>
            <div class="card">
                <h3>품목 및 금액 (카드형)</h3>
                <div style="background:#f9f9f9; padding:15px; border-radius:8px; margin-top:10px;">
                    <input type="text" class="input-field" placeholder="품목명">
                    <div style="display:flex; gap:10px;">
                        <input type="number" class="input-field" placeholder="수량">
                        <input type="number" class="input-field" placeholder="단가">
                    </div>
                </div>
                <button class="btn-primary" style="margin-top:15px;">발급하기</button>
            </div>
        """

    # Default Fallback (Generic Screen Design)
    else:
        content = f"""
            <div class="card" style="text-align:center; padding:40px 20px;">
                <i class="fa-solid fa-receipt" style="font-size:3rem; color:#aaa; margin-bottom:15px;"></i><br>
                <h3>{main_title} > {sub_title}</h3>
                <div style="margin-top:20px; text-align:left;">
                    <div style="padding:15px; background:#f9f9f9; border-radius:8px; margin-bottom:10px; color:#444;">
                        상세 내역 조회 <i class="fa-solid fa-chevron-right" style="float:right;"></i>
                    </div>
                    <div style="padding:15px; background:#f9f9f9; border-radius:8px; margin-bottom:10px; color:#444;">
                        처리 현황 <i class="fa-solid fa-chevron-right" style="float:right;"></i>
                    </div>
                    <button class="btn-primary" style="width:100%; margin-top:10px;">관련 신청서 작성</button>
                </div>
            </div>
        """

    return f"""
        <main class="page" id="{page_id}">
            <h2 class="page-title">{sub_title}</h2>
            {content}
            <!-- 빠른 이전가기 로직 -->
            <button class="btn-sm bg-gray nav-link" data-target="page-home" style="margin:20px 0; width:100%; padding:10px; display:block;">홈으로 돌아가기</button>
        </main>
    """

def build():
    sidebar_html = ""
    pages_html = ""
    
    for idx, menu in enumerate(menus):
        main_title = menu["main"]
        subs = menu["subs"]
        
        # Sidebar accordion item
        sidebar_html += f"""
            <div class="accordion-item">
                <div class="accordion-header">
                    <span>{main_title}</span>
                    <i class="fa-solid fa-chevron-down"></i>
                </div>
                <ul class="accordion-content">
        """
        
        # All sub items get a page
        for sub_idx, sub in enumerate(subs):
            page_id = f"page-gen-{idx}-{sub_idx}"
            sidebar_html += f'<li class="nav-link" data-target="{page_id}"><i class="fa-regular fa-circle-dot"></i> {sub}</li>\n'
            pages_html += generate_mock_page_content(idx, sub_idx, main_title, sub)
                
        sidebar_html += """
                </ul>
            </div>
        """

    # Generate Index HTML
    index_content = f"""<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>모바일 홈택스 (Mockup)</title>
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;500;700;900&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="app-container">
        <!-- 상단 헤더 -->
        <header class="header">
            <div class="header-left">
                <i class="fa-solid fa-bars menu-btn" id="menuToggle"></i>
                <div class="logo" id="logoHome">
                    <i class="fa-solid fa-house-chimney" style="color:#005bb8;"></i> 홈택스
                </div>
            </div>
            <div class="header-icons">
                <i class="fa-solid fa-microphone"></i>
                <i class="fa-regular fa-bell"></i>
            </div>
        </header>

        <!-- 사이드바 (Sitemap - 아코디언) -->
        <div class="sidebar-overlay" id="sidebarOverlay"></div>
        <nav class="sidebar" id="sidebar">
            <div class="sidebar-header">
                <h3>전체메뉴</h3>
                <i class="fa-solid fa-xmark close-btn" id="menuClose"></i>
            </div>
            <div class="sidebar-scroll">
                {sidebar_html}
            </div>
        </nav>

        <!-- PAGE: 메인 홈 -->
        <main class="page active" id="page-home">
            <section class="search-section">
                <div class="search-box">
                    <input type="text" placeholder="자연어 기반 지능형 검색 (예: 연말정산)">
                    <button class="search-btn"><i class="fa-solid fa-magnifying-glass"></i></button>
                    <button class="voice-btn"><i class="fa-solid fa-microphone-lines"></i></button>
                </div>
            </section>
            <section class="my-info card bg-gradient">
                <div class="profile-header text-white">
                    <div class="avatar bg-white text-blue"><i class="fa-solid fa-user"></i></div>
                    <div class="greeting">
                        <h2>홍길동 님</h2>
                        <p>간편인증 로그인 완료</p>
                    </div>
                </div>
            </section>
            
            <section class="favorite-services">
                <div class="section-title">
                    <h3>자주 찾는 서비스</h3>
                </div>
                <div class="service-grid">
                    <div class="service-icon-box nav-link" data-target="page-gen-0-0">
                        <div class="icon-circle bg-blue"><i class="fa-solid fa-file-invoice-dollar"></i></div>
                        <span>신고서조회</span>
                    </div>
                    <div class="service-icon-box nav-link" data-target="page-gen-1-0">
                        <div class="icon-circle bg-green"><i class="fa-solid fa-won-sign"></i></div>
                        <span>세금납부</span>
                    </div>
                    <div class="service-icon-box nav-link" data-target="page-gen-2-0">
                        <div class="icon-circle bg-orange"><i class="fa-solid fa-certificate"></i></div>
                        <span>즉시발급증명</span>
                    </div>
                    <div class="service-icon-box nav-link" data-target="page-gen-5-0">
                        <div class="icon-circle bg-purple"><i class="fa-solid fa-receipt"></i></div>
                        <span>전자계산서</span>
                    </div>
                </div>
            </section>
            
            <div class="card">
                <h3>안내</h3>
                <p style="color:#666; font-size:0.9rem; margin-top:5px;">
                   좌측 상단의 전체메뉴(≡)를 통해 대분류 및 <b>모든 중분류 화면</b>으로 개별 네비게이션이 가능합니다. 모든 메뉴가 구현되어 있습니다!
                </p>
            </div>
        </main>
        
        {pages_html}

        <!-- 하단 네비게이션 탭 -->
        <nav class="bottom-nav">
            <a href="#" class="nav-item active nav-link" data-target="page-home">
                <i class="fa-solid fa-house"></i>
                <span>홈</span>
            </a>
            <a href="#" class="nav-item nav-link" data-target="page-gen-0-0">
                <i class="fa-solid fa-file-invoice-dollar"></i>
                <span>세금신고</span>
            </a>
            <a href="#" class="nav-item scan-btn nav-link" data-target="page-home">
                <div class="scan-circle"><i class="fa-solid fa-qrcode"></i></div>
                <span>QR인증</span>
            </a>
            <a href="#" class="nav-item nav-link" data-target="page-gen-9-0">
                <i class="fa-solid fa-user-circle"></i>
                <span>My홈택스</span>
            </a>
            <a href="#" class="nav-item nav-link" data-target="page-gen-13-0">
                <i class="fa-solid fa-headset"></i>
                <span>고객센터</span>
            </a>
        </nav>
    </div>
    <script src="script.js"></script>
</body>
</html>
    """
    
    with open(r"d:\54. MyCoding\hometax\mobile_mockup\index.html", "w", encoding="utf-8") as f:
        f.write(index_content)

if __name__ == "__main__":
    build()
