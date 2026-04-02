import streamlit as st
import streamlit.components.v1 as components

# Cài đặt trang tràn viền tuyệt đối
st.set_page_config(layout="wide", page_title="Nguyen Hoang Minh - AI Portfolio", page_icon="✨", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
        .block-container { padding: 0 !important; max-width: 100% !important; overflow: hidden; }
        header { display: none !important; }
        footer { display: none !important; }
        iframe { border: none !important; height: 100vh !important; width: 100% !important; }
    </style>
""", unsafe_allow_html=True)

html_code = r"""
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Minh Nguyen | AI Portfolio</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        indigo: { 50: '#eef2ff', 100: '#e0e7ff', 500: '#6366f1', 600: '#4f46e5', 700: '#4338ca', 900: '#312e81' },
                        slate: { 50: '#f8fafc', 800: '#1e293b', 900: '#0f172a' }
                    }
                }
            }
        }
    </script>
</head>
<body class="bg-slate-50 text-slate-800 h-screen overflow-hidden font-sans selection:bg-indigo-200">

    <div class="flex flex-col md:flex-row h-full w-full mx-auto bg-white shadow-2xl relative">
        
        <div class="w-full md:w-1/2 h-1/3 md:h-full bg-gradient-to-br from-indigo-50/50 via-white to-slate-50 border-b md:border-r border-gray-100 flex flex-col p-8 md:p-12 relative overflow-y-auto" id="visual-panel">
            
            <div id="view-welcome" class="flex flex-col items-center justify-center h-full animate-fade-in transition-opacity duration-500">
                <div class="w-40 h-40 rounded-full bg-gradient-to-tr from-indigo-100 to-white border-4 border-white shadow-xl flex items-center justify-center mb-8 overflow-hidden relative group">
                    <span class="text-7xl group-hover:scale-110 transition-transform duration-300">👨‍💻</span>
                    <div class="absolute inset-0 rounded-full border-2 border-indigo-500/20 animate-ping"></div>
                </div>
                <h1 class="text-4xl font-extrabold text-slate-900 mb-2 tracking-tight">Nguyễn Hoàng Minh</h1>
                <h2 class="text-xl text-indigo-600 font-semibold mb-6 flex items-center gap-2">
                    <span class="w-2 h-2 rounded-full bg-indigo-600 animate-pulse"></span> Product Owner Intern
                </h2>
                <div class="flex flex-wrap justify-center gap-3 mb-8">
                    <span class="px-4 py-1.5 bg-white border border-slate-200 rounded-full text-sm font-medium text-slate-600 shadow-sm flex items-center gap-2">✉️ hwinh.work@gmail.com</span>
                    <span class="px-4 py-1.5 bg-white border border-slate-200 rounded-full text-sm font-medium text-slate-600 shadow-sm flex items-center gap-2">📞 +84 765 828 191</span>
                </div>
                <p class="text-center text-slate-500 max-w-md leading-relaxed">Khám phá hành trình kết nối giữa <b class="text-slate-700">Công nghệ thông minh</b> và <b class="text-slate-700">Trải nghiệm con người</b> qua lăng kính của Trợ lý AI bên phải.</p>
            </div>

            <div id="view-experience" class="hidden flex-col h-full animate-fade-in transition-opacity duration-500">
                <h2 class="text-3xl font-extrabold text-slate-900 mb-8 flex items-center gap-3"><span class="text-4xl">💼</span> Dấu ấn Sự nghiệp</h2>
                <div class="space-y-8 relative before:absolute before:inset-0 before:ml-5 before:-translate-x-px md:before:mx-auto md:before:translate-x-0 before:h-full before:w-0.5 before:bg-gradient-to-b before:from-indigo-100 before:via-indigo-300 before:to-transparent">
                    
                    <div class="relative flex items-center justify-between md:justify-normal md:odd:flex-row-reverse group is-active">
                        <div class="flex items-center justify-center w-10 h-10 rounded-full border-4 border-white bg-indigo-600 text-white shadow-lg shrink-0 md:order-1 md:group-odd:-translate-x-1/2 md:group-even:translate-x-1/2 z-10">🚀</div>
                        <div class="w-[calc(100%-4rem)] md:w-[calc(50%-2.5rem)] p-5 rounded-2xl border border-indigo-50 bg-white shadow-sm hover:shadow-xl transition-all duration-300 hover:-translate-y-1">
                            <div class="flex flex-col mb-3">
                                <span class="text-xs font-bold text-indigo-500 uppercase tracking-wider mb-1">08/2022 - Nay</span>
                                <h3 class="font-extrabold text-lg text-slate-900">Saigon Innovation Hub (SIHUB)</h3>
                                <p class="text-sm text-slate-500 font-medium">Project Management Executive</p>
                            </div>
                            <ul class="text-sm text-slate-600 space-y-2">
                                <li class="flex items-start gap-2"><span class="text-indigo-500">▹</span> Quản lý hành trình ươm tạo toàn diện cho tech-startups.</li>
                                <li class="flex items-start gap-2"><span class="text-indigo-500">▹</span> Kiến trúc Customer Journey Map, định hình luồng kích hoạt sản phẩm.</li>
                                <li class="flex items-start gap-2"><span class="text-indigo-500">▹</span> Triển khai A/B Testing, giải quyết triệt để các "pain points" của user.</li>
                            </ul>
                        </div>
                    </div>

                    <div class="relative flex items-center justify-between md:justify-normal md:odd:flex-row-reverse group is-active">
                        <div class="flex items-center justify-center w-10 h-10 rounded-full border-4 border-white bg-slate-300 text-slate-700 shadow-md shrink-0 md:order-1 md:group-odd:-translate-x-1/2 md:group-even:translate-x-1/2 z-10">🔬</div>
                        <div class="w-[calc(100%-4rem)] md:w-[calc(50%-2.5rem)] p-5 rounded-2xl border border-slate-100 bg-white shadow-sm hover:shadow-xl transition-all duration-300 hover:-translate-y-1">
                            <div class="flex flex-col mb-3">
                                <span class="text-xs font-bold text-slate-500 uppercase tracking-wider mb-1">07/2024 - 12/2024</span>
                                <h3 class="font-extrabold text-lg text-slate-900">Saigon Innovation Hub</h3>
                                <p class="text-sm text-slate-500 font-medium">R&D Intern</p>
                            </div>
                            <ul class="text-sm text-slate-600 space-y-2">
                                <li class="flex items-start gap-2"><span class="text-slate-400">▹</span> Dẫn dắt vòng đời dữ liệu đánh giá năng lực cấp thành phố.</li>
                                <li class="flex items-start gap-2"><span class="text-slate-400">▹</span> Điều phối chiến lược với hơn 150+ bên liên quan (stakeholders).</li>
                                <li class="flex items-start gap-2"><span class="text-slate-400">▹</span> Chuẩn hóa tài liệu hệ thống theo tiêu chuẩn URD khắt khe.</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>

            <div id="view-projects" class="hidden flex-col h-full animate-fade-in transition-opacity duration-500">
                <h2 class="text-3xl font-extrabold text-slate-900 mb-8 flex items-center gap-3"><span class="text-4xl">✨</span> Sản phẩm Tiêu biểu</h2>
                <div class="grid grid-cols-1 xl:grid-cols-2 gap-5 overflow-y-auto pr-2 pb-10">
                    
                    <div class="bg-white border border-slate-100 rounded-2xl p-6 shadow-sm hover:shadow-xl transition-all duration-300 hover:border-indigo-300 group">
                        <div class="flex justify-between items-start mb-3">
                            <div class="p-2 bg-indigo-50 rounded-lg group-hover:bg-indigo-600 transition-colors">
                                <span class="text-xl group-hover:text-white transition-colors">🧠</span>
                            </div>
                            <span class="text-xs bg-indigo-50 text-indigo-700 px-2.5 py-1 rounded-md font-bold">Deep Tech</span>
                        </div>
                        <h3 class="font-extrabold text-xl text-slate-900 mb-2">EchoMind AI System</h3>
                        <p class="text-sm text-slate-600 mb-5 leading-relaxed">Hệ thống giải mã tín hiệu não thành văn bản (Brain-to-Text). Tái cấu trúc mô hình Transformer, phá vỡ nút thắt thông tin, đạt vận tốc ấn tượng 55-65 WPM với độ trễ <1s.</p>
                        <div class="flex flex-wrap gap-2 mt-auto">
                            <span class="text-xs font-semibold bg-slate-100 text-slate-700 px-2.5 py-1 rounded-md">Python</span>
                            <span class="text-xs font-semibold bg-slate-100 text-slate-700 px-2.5 py-1 rounded-md">PyTorch</span>
                            <span class="text-xs font-semibold bg-slate-100 text-slate-700 px-2.5 py-1 rounded-md">System Architecture</span>
                        </div>
                    </div>

                    <div class="bg-white border border-slate-100 rounded-2xl p-6 shadow-sm hover:shadow-xl transition-all duration-300 hover:border-indigo-300 group">
                        <div class="flex justify-between items-start mb-3">
                            <div class="p-2 bg-indigo-50 rounded-lg group-hover:bg-indigo-600 transition-colors">
                                <span class="text-xl group-hover:text-white transition-colors">📱</span>
                            </div>
                            <span class="text-xs bg-amber-50 text-amber-700 px-2.5 py-1 rounded-md font-bold">Top 20 HCMC</span>
                        </div>
                        <h3 class="font-extrabold text-xl text-slate-900 mb-2">E-Reader Ecosystem</h3>
                        <p class="text-sm text-slate-600 mb-5 leading-relaxed">Ứng dụng triệt để nguyên lý Tương tác Người-Máy (HCI) thiết kế luồng kích hoạt sản phẩm. Giải quyết bài toán giảm thiểu ma sát và tải lượng nhận thức cho học sinh.</p>
                        <div class="flex flex-wrap gap-2 mt-auto">
                            <span class="text-xs font-semibold bg-slate-100 text-slate-700 px-2.5 py-1 rounded-md">UX/UI Design</span>
                            <span class="text-xs font-semibold bg-slate-100 text-slate-700 px-2.5 py-1 rounded-md">Journey Mapping</span>
                            <span class="text-xs font-semibold bg-slate-100 text-slate-700 px-2.5 py-1 rounded-md">HCI</span>
                        </div>
                    </div>
                </div>
            </div>

            <div id="view-skills" class="hidden flex-col h-full animate-fade-in transition-opacity duration-500 w-full items-center">
                <h2 class="text-3xl font-extrabold text-slate-900 mb-2 flex items-center gap-3 self-start"><span class="text-4xl">⚡</span> Năng lực Cốt lõi</h2>
                <p class="text-sm text-slate-500 mb-8 self-start">Sự giao thoa hoàn hảo giữa Tư duy Sản phẩm và Nền tảng Kỹ thuật.</p>
                
                <div class="w-full max-w-lg h-[400px] relative bg-white rounded-3xl p-6 shadow-sm border border-slate-100">
                    <canvas id="skillsChart"></canvas>
                </div>
                
                <div class="mt-8 flex flex-wrap justify-center gap-2.5 w-full max-w-lg">
                    <span class="px-4 py-1.5 bg-indigo-600 text-white rounded-lg text-sm font-semibold shadow-md">UX/UI Strategy</span>
                    <span class="px-4 py-1.5 bg-indigo-600 text-white rounded-lg text-sm font-semibold shadow-md">Agile/Scrum</span>
                    <span class="px-4 py-1.5 bg-indigo-600 text-white rounded-lg text-sm font-semibold shadow-md">A/B Testing</span>
                    <span class="px-4 py-1.5 bg-slate-800 text-white rounded-lg text-sm font-semibold">Data Analysis</span>
                    <span class="px-4 py-1.5 bg-slate-800 text-white rounded-lg text-sm font-semibold">Python</span>
                    <span class="px-4 py-1.5 bg-slate-800 text-white rounded-lg text-sm font-semibold">PyTorch</span>
                </div>
            </div>

            <div id="view-education" class="hidden flex-col h-full animate-fade-in transition-opacity duration-500">
                <h2 class="text-3xl font-extrabold text-slate-900 mb-8 flex items-center gap-3"><span class="text-4xl">🎓</span> Nền tảng Học thuật</h2>
                
                <div class="bg-gradient-to-br from-indigo-600 to-indigo-800 rounded-3xl p-8 text-white shadow-xl mb-6 relative overflow-hidden">
                    <div class="absolute top-0 right-0 -mt-4 -mr-4 w-32 h-32 bg-white opacity-10 rounded-full blur-2xl"></div>
                    <div class="flex justify-between items-start mb-6">
                        <div class="text-5xl">🏛️</div>
                        <span class="bg-white/20 px-3 py-1 rounded-full text-xs font-bold tracking-wider uppercase backdrop-blur-sm">Hiện tại</span>
                    </div>
                    <h3 class="text-2xl font-extrabold mb-2">Đại học Kinh tế TP.HCM (UEH)</h3>
                    <p class="text-indigo-100 font-medium mb-6 text-lg">Cử nhân Quản lý Công nghệ & Đổi mới Sáng tạo</p>
                    
                    <div class="flex items-center gap-4 bg-slate-900/40 p-4 rounded-2xl backdrop-blur-md w-fit border border-white/10">
                        <div class="p-2 bg-yellow-400/20 rounded-lg"><span class="text-2xl">🏆</span></div>
                        <div>
                            <p class="text-xs text-indigo-200 uppercase tracking-wide font-semibold mb-0.5">Thành tích học tập (GPA)</p>
                            <p class="font-black text-2xl tracking-tight">3.53 <span class="text-indigo-300 text-lg font-medium">/ 4.0</span></p>
                        </div>
                    </div>
                </div>
                
                <div class="grid grid-cols-2 gap-4">
                    <div class="bg-white rounded-2xl border border-slate-100 p-5 shadow-sm">
                        <div class="text-2xl mb-2">🏅</div>
                        <h4 class="font-bold text-slate-900 mb-1">Google Certifications</h4>
                        <p class="text-xs text-slate-500">Project Management & Business Intelligence</p>
                    </div>
                    <div class="bg-white rounded-2xl border border-slate-100 p-5 shadow-sm">
                        <div class="text-2xl mb-2">🎯</div>
                        <h4 class="font-bold text-slate-900 mb-1">Professional Dev</h4>
                        <p class="text-xs text-slate-500">Agile Management & Vingroup AI Talent Prep</p>
                    </div>
                </div>
            </div>
        </div>

        <div class="w-full md:w-1/2 h-2/3 md:h-full bg-slate-50 flex flex-col relative border-l border-slate-200">
            
            <div class="h-[72px] border-b border-slate-200 flex items-center px-6 bg-white shrink-0 z-10 shadow-sm justify-between">
                <div class="flex items-center gap-4">
                    <div class="w-12 h-12 rounded-full bg-gradient-to-tr from-indigo-100 to-indigo-50 flex items-center justify-center relative shadow-inner">
                        <span class="text-2xl">🤖</span>
                        <span class="absolute bottom-0 right-0 w-3.5 h-3.5 bg-emerald-500 border-2 border-white rounded-full"></span>
                    </div>
                    <div>
                        <h2 class="font-extrabold text-slate-900 text-lg leading-tight">Minh's AI Proxy</h2>
                        <p class="text-xs text-emerald-600 font-semibold flex items-center gap-1"><span class="w-1.5 h-1.5 rounded-full bg-emerald-500 animate-pulse"></span> Sẵn sàng kết nối</p>
                    </div>
                </div>
                <button onclick="resetChat()" class="text-sm p-2 text-slate-400 hover:text-indigo-600 hover:bg-indigo-50 rounded-lg transition-all" title="Làm mới cuộc trò chuyện">
                    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 12a9 9 0 1 0 9-9 9.75 9.75 0 0 0-6.74 2.74L3 8"/><path d="M3 3v5h5"/></svg>
                </button>
            </div>

            <div id="chat-messages" class="flex-1 overflow-y-auto p-6 space-y-6 scroll-smooth pb-32">
                </div>
            
            <div id="typing-indicator" class="hidden absolute bottom-[100px] left-6 msg-ai px-4 py-3 rounded-2xl shadow-sm border border-slate-100 bg-white items-center gap-1.5">
                <div class="w-2 h-2 bg-indigo-400 rounded-full animate-bounce"></div>
                <div class="w-2 h-2 bg-indigo-400 rounded-full animate-bounce" style="animation-delay: 0.15s"></div>
                <div class="w-2 h-2 bg-indigo-400 rounded-full animate-bounce" style="animation-delay: 0.3s"></div>
            </div>

            <div class="absolute bottom-0 left-0 w-full bg-gradient-to-t from-slate-50 via-slate-50 to-transparent pt-12 pb-6 px-6 shrink-0">
                <div id="quick-prompts" class="flex flex-wrap gap-2.5 justify-end transition-opacity duration-300">
                    </div>
            </div>

        </div>
    </div>

    <style>
        @keyframes fadeIn { from { opacity: 0; transform: translateY(15px); } to { opacity: 1; transform: translateY(0); } }
        .animate-fade-in { animation: fadeIn 0.5s cubic-bezier(0.4, 0, 0.2, 1) forwards; }
        
        @keyframes blink { 0%, 100% { opacity: 1; } 50% { opacity: 0; } }
        .cursor-blink { display: inline-block; width: 6px; height: 16px; background-color: #4f46e5; margin-left: 4px; animation: blink 1s step-end infinite; vertical-align: middle; border-radius: 2px;}
        
        ::-webkit-scrollbar { width: 6px; }
        ::-webkit-scrollbar-track { background: transparent; }
        ::-webkit-scrollbar-thumb { background: #cbd5e1; border-radius: 10px; }
        ::-webkit-scrollbar-thumb:hover { background: #94a3b8; }

        /* Bong bóng chat siêu mượt */
        .msg-ai { background-color: #ffffff; color: #1e293b; border: 1px solid #f1f5f9; border-bottom-left-radius: 4px; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05); border-top-left-radius: 16px; border-top-right-radius: 16px; border-bottom-right-radius: 16px;}
        .msg-user { background-color: #4f46e5; color: #ffffff; border-bottom-right-radius: 4px; box-shadow: 0 4px 6px -1px rgba(79, 70, 229, 0.3); border-top-left-radius: 16px; border-top-right-radius: 16px; border-bottom-left-radius: 16px;}
    </style>

    <script>
        // Nội dung chuẩn chỉnh của AI
        const cvData = {
            greeting: `Chào Quý Nhà tuyển dụng! Tôi là Đặc vụ AI đại diện cho Nguyễn Hoàng Minh (hwinh).\n\nMinh là một chuyên gia Quản lý Sản phẩm (Product Owner Intern) với năng lực cốt lõi là tối ưu hóa Trải nghiệm Người dùng (UX) và kiến trúc hệ thống.\n\nNgài muốn khám phá khía cạnh nào trong hồ sơ năng lực của Minh? Xin mời đưa ra chỉ thị bên dưới.`,
            
            experience: `Hành trình sự nghiệp của Minh tập trung vào việc kiến tạo hệ sinh thái công nghệ:\n\nTừ 08/2022 đến nay, tại Saigon Innovation Hub (SIHUB), Minh đóng vai trò thiết kế Customer Journey Map và định hình các luồng MVP cho startup.\n\nĐiểm sáng nhất là việc Minh áp dụng tư duy dữ liệu (A/B Testing, Interleaving) để giải quyết triệt để các "nỗi đau" (pain points) của người dùng trước khi tung sản phẩm ra thị trường rộng lớn.\n\nMời Ngài xem chi tiết mốc thời gian ở bảng bên trái.`,
            
            projects: `Sản phẩm của Minh là minh chứng cho việc hòa quyện giữa Deep-tech và UX.\n\nDự án 'EchoMind AI' thể hiện tư duy kiến trúc hệ thống xuất sắc khi Minh tối ưu mô hình Transformer bằng PyTorch, đẩy tốc độ giải mã tín hiệu não lên 55-65 WPM với độ trễ cực thấp.\n\nBên cạnh đó, 'E-Reader Ecosystem' (Top 20 TP.HCM) là một bài toán thành công về việc áp dụng nguyên lý HCI để giảm tải nhận thức cho người dùng cuối.\n\nChi tiết công nghệ (Tech Stack) đang hiển thị ở thẻ bên trái.`,
            
            skills: `Ngài đang xem biểu đồ năng lực đa chiều của Minh.\n\nThay vì chỉ tập trung vào một công đoạn, Minh sở hữu tầm nhìn bao quát toàn bộ vòng đời sản phẩm: Từ việc thấu cảm người dùng (UX Design, Journey Mapping), điều phối thực thi (Agile/Scrum), cho đến kiểm chứng tính khả thi bằng công nghệ lõi (Python, PyTorch, Data Analysis).\n\nSự giao thoa này giúp Minh đưa ra các quyết định làm sản phẩm cực kỳ sắc bén và thực tế.`,
            
            education: `Nền tảng học thuật của Minh cực kỳ vững chắc.\n\nLà sinh viên năm cuối ngành Quản lý Công nghệ & Đổi mới Sáng tạo tại Đại học Kinh tế TP.HCM, Minh duy trì mức GPA ấn tượng 3.53/4.0.\n\nKhông dừng lại ở trường lớp, Minh liên tục nâng cấp bản thân với các chứng chỉ chuyên sâu từ Google (Project Management, BI) và đang rèn luyện gắt gao cho chương trình AI Thực Chiến của Vingroup.`
        };

        const prompts = [
            { id: 'experience', label: '💼 Dấu ấn Sự nghiệp', type: 'primary' },
            { id: 'projects', label: '✨ Sản phẩm Tiêu biểu', type: 'primary' },
            { id: 'skills', label: '⚡ Năng lực Cốt lõi', type: 'primary' },
            { id: 'education', label: '🎓 Học vấn & Chứng chỉ', type: 'secondary' }
        ];

        let isTyping = false;
        let chartInstance = null;

        const chatContainer = document.getElementById('chat-messages');
        const promptsContainer = document.getElementById('quick-prompts');
        const typingIndicator = document.getElementById('typing-indicator');
        const views = {
            welcome: document.getElementById('view-welcome'),
            experience: document.getElementById('view-experience'),
            projects: document.getElementById('view-projects'),
            skills: document.getElementById('view-skills'),
            education: document.getElementById('view-education')
        };

        function initChat() {
            chatContainer.innerHTML = '';
            renderPrompts();
            switchView('welcome');
            setTimeout(() => { appendMessage('ai', cvData.greeting, true); }, 600);
        }

        function renderPrompts() {
            promptsContainer.innerHTML = prompts.map(p => {
                const bgClass = p.type === 'primary' 
                    ? 'bg-indigo-50 text-indigo-700 border-indigo-200 hover:bg-indigo-600 hover:text-white hover:border-indigo-600' 
                    : 'bg-white text-slate-600 border-slate-200 hover:bg-slate-800 hover:text-white hover:border-slate-800';
                return `<button onclick="handlePromptClick('${p.id}', '${p.label}')" class="px-5 py-2.5 rounded-full border text-[13px] font-bold transition-all duration-300 shadow-sm hover:shadow-md ${bgClass}" ${isTyping ? 'disabled' : ''}>${p.label}</button>`;
            }).join('');
        }

        function switchView(viewId) {
            Object.values(views).forEach(el => { el.classList.add('hidden'); el.classList.remove('flex'); });
            views[viewId].classList.remove('hidden'); views[viewId].classList.add('flex');
            if (viewId === 'skills') renderSkillsChart();
        }

        function handlePromptClick(promptId, promptLabel) {
            if (isTyping) return;
            isTyping = true;
            promptsContainer.style.opacity = '0';
            setTimeout(() => { promptsContainer.style.display = 'none'; }, 300);

            // Hiện câu hỏi của User
            appendMessage('user', promptLabel, false);

            // Hiện hiệu ứng "AI đang suy nghĩ..."
            setTimeout(() => {
                typingIndicator.classList.remove('hidden');
                typingIndicator.classList.add('flex');
                scrollToBottom();
                
                // Sau 1 giây suy nghĩ, mới bắt đầu trả lời và chuyển view
                setTimeout(() => {
                    typingIndicator.classList.add('hidden');
                    typingIndicator.classList.remove('flex');
                    switchView(promptId);
                    
                    appendMessage('ai', cvData[promptId], true, () => {
                        promptsContainer.style.display = 'flex';
                        setTimeout(() => { promptsContainer.style.opacity = '1'; }, 50);
                    });
                }, 1000);
            }, 500);
        }

        function appendMessage(sender, text, useTypewriter = false, callback = null) {
            const msgDiv = document.createElement('div');
            msgDiv.className = `flex w-full ${sender === 'user' ? 'justify-end' : 'justify-start'} animate-fade-in`;
            
            const innerDiv = document.createElement('div');
            innerDiv.className = `max-w-[85%] md:max-w-[80%] px-5 py-3.5 text-[14.5px] leading-relaxed font-medium ${sender === 'user' ? 'msg-user' : 'msg-ai'}`;
            
            if (sender === 'ai' && useTypewriter) {
                msgDiv.appendChild(innerDiv);
                chatContainer.appendChild(msgDiv);
                typeWriter(text, innerDiv, 15, callback); // Gõ cực nhanh và mượt
            } else {
                innerDiv.innerHTML = text.replace(/\n/g, '<br><br>');
                msgDiv.appendChild(innerDiv);
                chatContainer.appendChild(msgDiv);
                scrollToBottom();
                if (callback) callback();
            }
        }

        function typeWriter(text, element, speed, callback) {
            let i = 0;
            element.innerHTML = '<span class="text-content"></span><span class="cursor-blink"></span>';
            const textContainer = element.querySelector('.text-content');
            
            function type() {
                if (i < text.length) {
                    let char = text.charAt(i);
                    if (char === '\n') {
                        textContainer.innerHTML += '<br>';
                        if(text.charAt(i+1) === '\n') { textContainer.innerHTML += '<br>'; i++; } // Xử lý 2 dòng trống
                    } else {
                        textContainer.innerHTML += char;
                    }
                    i++;
                    scrollToBottom();
                    setTimeout(type, speed);
                } else {
                    isTyping = false;
                    element.querySelector('.cursor-blink').remove();
                    if (callback) callback();
                }
            }
            type();
        }

        function scrollToBottom() {
            chatContainer.scrollTop = chatContainer.scrollHeight + 100;
        }

        function resetChat() {
            if(isTyping) return;
            initChat();
        }

        // Radar Chart cao cấp với tông Xanh chàm (Indigo)
        function renderSkillsChart() {
            const ctx = document.getElementById('skillsChart');
            if (chartInstance) chartInstance.destroy();

            chartInstance = new Chart(ctx, {
                type: 'radar',
                data: {
                    labels: ['UX/UI Design', 'Agile/Scrum', 'Journey Mapping', 'Data Analysis', 'Python', 'PyTorch', 'A/B Testing'],
                    datasets: [{
                        label: 'Độ thông thạo',
                        data: [90, 85, 95, 80, 80, 75, 85],
                        fill: true,
                        backgroundColor: 'rgba(79, 70, 229, 0.2)', 
                        borderColor: 'rgba(79, 70, 229, 1)',
                        borderWidth: 2,
                        pointBackgroundColor: 'rgba(79, 70, 229, 1)',
                        pointBorderColor: '#fff',
                        pointHoverBackgroundColor: '#fff',
                        pointHoverBorderColor: 'rgba(79, 70, 229, 1)',
                        pointRadius: 4,
                        pointHoverRadius: 6
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    scales: {
                        r: {
                            angleLines: { color: 'rgba(15, 23, 42, 0.05)' },
                            grid: { color: 'rgba(15, 23, 42, 0.05)' },
                            pointLabels: {
                                font: { size: 12, family: "'Inter', sans-serif", weight: '700' },
                                color: '#1e293b' 
                            },
                            ticks: { display: false, min: 0, max: 100, stepSize: 20 }
                        }
                    },
                    plugins: {
                        legend: { display: false },
                        tooltip: {
                            backgroundColor: 'rgba(15, 23, 42, 0.95)',
                            titleFont: { size: 13, family: "'Inter', sans-serif" },
                            bodyFont: { size: 14, weight: 'bold' },
                            padding: 12,
                            cornerRadius: 8,
                            callbacks: {
                                label: function(context) {
                                    let val = context.raw;
                                    if(val >= 90) return ' Mức độ: Xuất sắc';
                                    if(val >= 80) return ' Mức độ: Rất Tốt';
                                    return ' Mức độ: Tốt';
                                }
                            }
                        }
                    }
                }
            });
        }

        window.addEventListener('DOMContentLoaded', initChat);
    </script>
</body>
</html>
"""

# Gọi thành phần Streamlit render HTML với chiều cao tối đa
components.html(html_code, height=950, scrolling=True)
