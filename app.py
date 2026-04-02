import streamlit as st
import streamlit.components.v1 as components

# Cài đặt trang Streamlit chiếm toàn màn hình
st.set_page_config(layout="wide", page_title="Nguyễn Hoàng Minh - AI Portfolio", initial_sidebar_state="collapsed")

# Chứa toàn bộ mã HTML/CSS/JS đã được điền thông tin CV của bạn
html_code = """
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Nguyễn Hoàng Minh | AI Portfolio</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
</head>
<body class="bg-gray-50 text-slate-800 h-screen overflow-hidden font-sans selection:bg-blue-200">

    <div class="flex flex-col md:flex-row h-full w-full max-w-[1600px] mx-auto bg-white shadow-2xl relative">
        
        <div class="w-full md:w-1/2 h-1/3 md:h-full bg-gradient-to-br from-blue-50 to-white border-b md:border-r border-gray-200 flex flex-col p-8 relative overflow-y-auto" id="visual-panel">
            
            <div id="view-welcome" class="flex flex-col items-center justify-center h-full animate-fade-in transition-opacity duration-500">
                <div class="w-40 h-40 rounded-full bg-blue-100 border-4 border-white shadow-xl flex items-center justify-center mb-6 overflow-hidden">
                    <span class="text-6xl">👨‍💻</span>
                </div>
                <h1 class="text-3xl font-bold text-slate-800 mb-2">Nguyễn Hoàng Minh (hwinh)</h1>
                <h2 class="text-xl text-blue-600 font-medium mb-4">Product Owner Intern</h2>
                <div class="flex flex-wrap justify-center gap-2 mb-6">
                    <span class="px-3 py-1 bg-white border border-gray-200 rounded-full text-sm shadow-sm">hwinh.work@gmail.com</span>
                    <span class="px-3 py-1 bg-white border border-gray-200 rounded-full text-sm shadow-sm">+84 765828191</span>
                    <span class="px-3 py-1 bg-white border border-gray-200 rounded-full text-sm shadow-sm">Hồ Chí Minh</span>
                </div>
                <p class="text-center text-slate-500 max-w-md">Bắt đầu trò chuyện với Trợ lý AI bên phải để khám phá chi tiết về kinh nghiệm và tư duy thiết kế của tôi.</p>
            </div>

            <div id="view-experience" class="hidden flex-col h-full animate-fade-in transition-opacity duration-500">
                <h2 class="text-2xl font-bold text-slate-800 mb-6 flex items-center gap-2"><span class="text-3xl">💼</span> Kinh nghiệm làm việc</h2>
                <div class="space-y-6 relative before:absolute before:inset-0 before:ml-5 before:-translate-x-px md:before:mx-auto md:before:translate-x-0 before:h-full before:w-0.5 before:bg-gradient-to-b before:from-transparent before:via-blue-300 before:to-transparent">
                    
                    <div class="relative flex items-center justify-between md:justify-normal md:odd:flex-row-reverse group is-active">
                        <div class="flex items-center justify-center w-10 h-10 rounded-full border-4 border-white bg-blue-500 text-white shadow shrink-0 md:order-1 md:group-odd:-translate-x-1/2 md:group-even:translate-x-1/2 z-10">
                            🚀
                        </div>
                        <div class="w-[calc(100%-4rem)] md:w-[calc(50%-2.5rem)] p-4 rounded-xl border border-blue-100 bg-white shadow-sm transition hover:shadow-md">
                            <div class="flex items-center justify-between mb-1">
                                <h3 class="font-bold text-lg text-slate-800">SIHUB</h3>
                                <time class="text-xs font-medium text-blue-500 bg-blue-50 px-2 py-1 rounded">08/2022 - Nay</time>
                            </div>
                            <p class="text-sm text-slate-500 font-medium mb-2">Project Management Executive</p>
                            <ul class="text-sm text-slate-600 list-disc pl-4 space-y-1">
                                <li>Quản lý hành trình ươm tạo startup công nghệ.</li>
                                <li>Thiết kế Customer Journey Map và định hướng MVP.</li>
                                <li>Áp dụng A/B Testing tối ưu hóa trải nghiệm.</li>
                            </ul>
                        </div>
                    </div>

                    <div class="relative flex items-center justify-between md:justify-normal md:odd:flex-row-reverse group is-active">
                        <div class="flex items-center justify-center w-10 h-10 rounded-full border-4 border-white bg-slate-300 text-white shadow shrink-0 md:order-1 md:group-odd:-translate-x-1/2 md:group-even:translate-x-1/2 z-10">
                            🔬
                        </div>
                        <div class="w-[calc(100%-4rem)] md:w-[calc(50%-2.5rem)] p-4 rounded-xl border border-gray-100 bg-white shadow-sm transition hover:shadow-md">
                            <div class="flex items-center justify-between mb-1">
                                <h3 class="font-bold text-lg text-slate-800">SIHUB</h3>
                                <time class="text-xs font-medium text-slate-500 bg-slate-50 px-2 py-1 rounded">07/2024 - 12/2024</time>
                            </div>
                            <p class="text-sm text-slate-500 font-medium mb-2">R&D Intern</p>
                            <ul class="text-sm text-slate-600 list-disc pl-4 space-y-1">
                                <li>Phân tích dữ liệu vòng đời cấp thành phố.</li>
                                <li>Làm việc trực tiếp với 150+ bên liên quan.</li>
                                <li>Tài liệu hóa theo tiêu chuẩn URD khắt khe.</li>
                            </ul>
                        </div>
                    </div>

                </div>
            </div>

            <div id="view-projects" class="hidden flex-col h-full animate-fade-in transition-opacity duration-500">
                <h2 class="text-2xl font-bold text-slate-800 mb-6 flex items-center gap-2"><span class="text-3xl">🚀</span> Dự án nổi bật</h2>
                <div class="grid grid-cols-1 xl:grid-cols-2 gap-4 overflow-y-auto pr-2 pb-10">
                    
                    <div class="bg-white border border-gray-200 rounded-xl p-5 shadow-sm hover:shadow-lg transition hover:border-blue-300 cursor-pointer">
                        <div class="flex justify-between items-start mb-2">
                            <h3 class="font-bold text-xl text-blue-700">EchoMind AI</h3>
                            <span class="text-xs bg-green-100 text-green-700 px-2 py-1 rounded font-bold">09/2025 - 12/2025</span>
                        </div>
                        <p class="text-sm text-slate-600 mb-4 line-clamp-3">Hệ thống chuyển đổi tín hiệu não thành văn bản (Brain-to-Text). Tối ưu hóa kiến trúc Transformer, đạt tốc độ giải mã 55-65 WPM với độ trễ siêu thấp.</p>
                        <div class="flex flex-wrap gap-2 mt-auto">
                            <span class="text-xs font-medium bg-blue-50 text-blue-600 px-2 py-1 rounded">Python</span>
                            <span class="text-xs font-medium bg-blue-50 text-blue-600 px-2 py-1 rounded">PyTorch</span>
                            <span class="text-xs font-medium bg-blue-50 text-blue-600 px-2 py-1 rounded">System Logic</span>
                        </div>
                    </div>

                    <div class="bg-white border border-gray-200 rounded-xl p-5 shadow-sm hover:shadow-lg transition hover:border-blue-300 cursor-pointer">
                        <div class="flex justify-between items-start mb-2">
                            <h3 class="font-bold text-xl text-blue-700">E-Reader Ecosystem</h3>
                            <span class="text-xs bg-gray-100 text-gray-700 px-2 py-1 rounded font-bold">03/2025 - 06/2025</span>
                        </div>
                        <p class="text-sm text-slate-600 mb-4 line-clamp-3">Hệ sinh thái Giáo dục số lọt Top 20 Chung cuộc. Ứng dụng nguyên lý Tương tác Người-Máy (HCI) để giảm tải nhận thức và ma sát cho học sinh.</p>
                        <div class="flex flex-wrap gap-2 mt-auto">
                            <span class="text-xs font-medium bg-blue-50 text-blue-600 px-2 py-1 rounded">UX/UI</span>
                            <span class="text-xs font-medium bg-blue-50 text-blue-600 px-2 py-1 rounded">Journey Mapping</span>
                            <span class="text-xs font-medium bg-blue-50 text-blue-600 px-2 py-1 rounded">HCI</span>
                        </div>
                    </div>

                </div>
            </div>

            <div id="view-skills" class="hidden flex-col h-full animate-fade-in transition-opacity duration-500 w-full items-center">
                <h2 class="text-2xl font-bold text-slate-800 mb-2 flex items-center gap-2 self-start"><span class="text-3xl">⚡</span> Kỹ năng chuyên môn</h2>
                <p class="text-sm text-slate-500 mb-6 self-start">Mức độ thành thạo các kỹ năng và công nghệ hiện tại.</p>
                <div class="chart-container w-full max-w-md h-[350px] relative">
                    <canvas id="skillsChart"></canvas>
                </div>
                <div class="mt-6 flex flex-wrap justify-center gap-2">
                    <span class="px-3 py-1 bg-slate-800 text-white rounded text-sm font-medium">Agile/Scrum</span>
                    <span class="px-3 py-1 bg-slate-800 text-white rounded text-sm font-medium">UX Design</span>
                    <span class="px-3 py-1 bg-slate-800 text-white rounded text-sm font-medium">Journey Mapping</span>
                    <span class="px-3 py-1 border border-slate-300 text-slate-600 rounded text-sm">Python</span>
                    <span class="px-3 py-1 border border-slate-300 text-slate-600 rounded text-sm">PyTorch</span>
                    <span class="px-3 py-1 border border-slate-300 text-slate-600 rounded text-sm">A/B Testing</span>
                </div>
            </div>

            <div id="view-education" class="hidden flex-col h-full animate-fade-in transition-opacity duration-500">
                <h2 class="text-2xl font-bold text-slate-800 mb-6 flex items-center gap-2"><span class="text-3xl">📚</span> Học vấn & Thành tích</h2>
                
                <div class="bg-gradient-to-r from-blue-600 to-blue-400 rounded-2xl p-6 text-white shadow-lg mb-6">
                    <div class="flex justify-between items-center mb-4">
                        <div class="text-4xl">🏛️</div>
                        <div class="text-right">
                            <span class="text-blue-100 text-sm">Hiện tại</span>
                        </div>
                    </div>
                    <h3 class="text-2xl font-bold mb-1">Đại học Kinh tế TP.HCM (UEH)</h3>
                    <p class="text-blue-100 font-medium mb-4">Cử nhân Quản lý Công nghệ và Đổi mới sáng tạo</p>
                    <div class="flex items-center gap-3 bg-white/20 p-3 rounded-lg backdrop-blur-sm w-fit">
                        <span class="text-xl">🏆</span>
                        <div>
                            <p class="text-xs text-blue-100">Điểm trung bình (GPA)</p>
                            <p class="font-bold text-lg">3.53 / 4.0</p>
                        </div>
                    </div>
                </div>
                <div class="bg-white rounded-xl border border-gray-100 p-5 shadow-sm">
                    <h4 class="font-bold text-slate-800 mb-3">Chứng chỉ & Khóa học nổi bật</h4>
                    <ul class="text-slate-600 list-disc pl-5 space-y-2">
                        <li>Google Project Management</li>
                        <li>Google Business Intelligence</li>
                        <li>Agile Management</li>
                    </ul>
                </div>
            </div>

        </div>

        <div class="w-full md:w-1/2 h-2/3 md:h-full bg-white flex flex-col relative">
            
            <div class="h-16 border-b border-gray-100 flex items-center px-6 bg-white shrink-0 z-10 shadow-sm">
                <div class="w-10 h-10 rounded-full bg-blue-100 flex items-center justify-center mr-3 relative">
                    <span class="text-xl">🤖</span>
                    <span class="absolute bottom-0 right-0 w-3 h-3 bg-green-500 border-2 border-white rounded-full"></span>
                </div>
                <div>
                    <h2 class="font-bold text-slate-800 leading-tight">Minh's AI Assistant</h2>
                    <p class="text-xs text-green-500 font-medium">Đang trực tuyến</p>
                </div>
                <button onclick="resetChat()" class="ml-auto text-sm text-slate-400 hover:text-blue-600 transition" title="Làm mới cuộc trò chuyện">🔄 Khởi động lại</button>
            </div>

            <div id="chat-messages" class="flex-1 overflow-y-auto p-6 space-y-6 scroll-smooth pb-32">
                </div>

            <div class="absolute bottom-0 left-0 w-full bg-gradient-to-t from-white via-white to-transparent pt-10 pb-6 px-6 shrink-0">
                <div id="quick-prompts" class="flex flex-wrap gap-2 justify-end transition-opacity duration-300">
                    </div>
            </div>

        </div>
    </div>

    <style>
        @keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }
        .animate-fade-in { animation: fadeIn 0.4s ease-out forwards; }
        
        @keyframes blink { 0%, 100% { opacity: 1; } 50% { opacity: 0; } }
        .cursor-blink { display: inline-block; width: 8px; height: 16px; background-color: #2563eb; margin-left: 2px; animation: blink 1s step-end infinite; vertical-align: middle; }
        
        ::-webkit-scrollbar { width: 6px; }
        ::-webkit-scrollbar-track { background: transparent; }
        ::-webkit-scrollbar-thumb { background: #cbd5e1; border-radius: 10px; }
        ::-webkit-scrollbar-thumb:hover { background: #94a3b8; }

        .msg-ai { background-color: #ffffff; color: #1e293b; border: 1px solid #e2e8f0; border-bottom-left-radius: 4px; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05); }
        .msg-user { background-color: #2563eb; color: #ffffff; border-bottom-right-radius: 4px; box-shadow: 0 4px 6px -1px rgba(59, 130, 246, 0.3); }
        .chart-container { margin: 0 auto; width: 100%; }
    </style>

    <script>
        // Dữ liệu nội dung của AI
        const cvData = {
            greeting: "Chào Quý Nhà tuyển dụng! Tôi là trợ lý AI đại diện cho Nguyễn Hoàng Minh (hwinh). Minh là một Product Owner Intern đầy nhiệt huyết, đam mê giải quyết vấn đề hệ thống và tối ưu hóa UX. Mời bạn chọn các chủ đề bên dưới để khám phá hồ sơ của Minh nhé!",
            experience: "Về kinh nghiệm làm việc:\\nMinh hiện đang làm Project Management Executive tại SIHUB. Tại đây, Minh quản lý toàn bộ hành trình ươm tạo, thiết kế bản đồ hành trình số (Customer Journey Mapping) và phân tích các điểm chạm (touchpoints).\\n\\nTrước đó (07/2024 - 12/2024), Minh làm R&D Intern, phụ trách thu thập dữ liệu và phân tích khoảng trống năng lực cho dự án cấp thành phố với hơn 150 bên liên quan. Mời bạn xem timeline chi tiết ở màn hình bên trái!",
            projects: "Các dự án nổi bật chứng minh năng lực kết hợp Sản phẩm và Công nghệ của Minh.\\n\\nNổi bật là 'EchoMind' - Hệ thống AI chuyển đổi tín hiệu não thành văn bản dùng PyTorch, đạt tốc độ giải mã 55-65 WPM. Bên cạnh đó, dự án 'E-Reader' lọt Top 20 chung cuộc TP.HCM đã áp dụng sâu sắc các nguyên lý HCI.\\n\\nHãy click vào danh sách bên trái để xem mô tả nhé!",
            skills: "Minh sở hữu bộ kỹ năng đa dạng.\\n\\nThế mạnh cốt lõi là tư duy Agile/Scrum, thiết kế trải nghiệm người dùng (UX) và thử nghiệm A/B. Về kỹ thuật, Minh có nền tảng vững về Python và Data Analysis.\\n\\nBiểu đồ Radar bên trái sẽ cho bạn cái nhìn trực quan nhất về mức độ tự tin của Minh.",
            education: "Về học vấn:\\nMinh đang theo học Cử nhân ngành Quản lý Công nghệ & Đổi mới Sáng tạo tại Đại học Kinh tế TP.HCM (UEH).\\n\\nMinh đạt điểm GPA xuất sắc 3.53/4.0. Ngoài ra, Minh còn tích lũy các chứng chỉ chuyên nghiệp của Google về Project Management."
        };

        const prompts = [
            { id: 'experience', label: '💼 Kinh nghiệm làm việc', type: 'primary' },
            { id: 'projects', label: '🚀 Các dự án nổi bật', type: 'primary' },
            { id: 'skills', label: '⚡ Kỹ năng công nghệ', type: 'primary' },
            { id: 'education', label: '📚 Học vấn & Thành tích', type: 'secondary' }
        ];

        let isTyping = false;
        let chartInstance = null;

        const chatContainer = document.getElementById('chat-messages');
        const promptsContainer = document.getElementById('quick-prompts');
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
            setTimeout(() => {
                appendMessage('ai', cvData.greeting, true);
            }, 500);
        }

        function renderPrompts() {
            promptsContainer.innerHTML = prompts.map(p => {
                const bgClass = p.type === 'primary' 
                    ? 'bg-blue-50 text-blue-700 border-blue-200 hover:bg-blue-600 hover:text-white' 
                    : 'bg-white text-slate-600 border-gray-200 hover:bg-slate-800 hover:text-white hover:border-slate-800';
                return `<button onclick="handlePromptClick('${p.id}', '${p.label}')" class="px-4 py-2 rounded-full border text-sm font-medium transition-colors duration-200 shadow-sm ${bgClass}" ${isTyping ? 'disabled' : ''}>${p.label}</button>`;
            }).join('');
        }

        function switchView(viewId) {
            Object.values(views).forEach(el => {
                el.classList.add('hidden');
                el.classList.remove('flex');
            });
            views[viewId].classList.remove('hidden');
            views[viewId].classList.add('flex');

            if (viewId === 'skills') {
                renderSkillsChart();
            }
        }

        function handlePromptClick(promptId, promptLabel) {
            if (isTyping) return;
            promptsContainer.style.opacity = '0';
            setTimeout(() => { promptsContainer.style.display = 'none'; }, 300);
            appendMessage('user', promptLabel, false);
            setTimeout(() => {
                switchView(promptId);
                appendMessage('ai', cvData[promptId], true, () => {
                    promptsContainer.style.display = 'flex';
                    setTimeout(() => { promptsContainer.style.opacity = '1'; }, 50);
                });
            }, 600);
        }

        function appendMessage(sender, text, useTypewriter = false, callback = null) {
            const msgDiv = document.createElement('div');
            msgDiv.className = `flex w-full ${sender === 'user' ? 'justify-end' : 'justify-start'} animate-fade-in`;
            const innerDiv = document.createElement('div');
            innerDiv.className = `max-w-[85%] md:max-w-[75%] rounded-2xl px-5 py-3 text-[15px] leading-relaxed ${sender === 'user' ? 'msg-user' : 'msg-ai'}`;
            
            if (sender === 'ai' && useTypewriter) {
                msgDiv.appendChild(innerDiv);
                chatContainer.appendChild(msgDiv);
                typeWriter(text, innerDiv, 20, callback);
            } else {
                innerDiv.innerHTML = text.replace(/\\n/g, '<br>');
                msgDiv.appendChild(innerDiv);
                chatContainer.appendChild(msgDiv);
                scrollToBottom();
                if (callback) callback();
            }
        }

        function typeWriter(text, element, speed, callback) {
            isTyping = true;
            renderPrompts(); 
            let i = 0;
            element.innerHTML = '<span class="text-content"></span><span class="cursor-blink"></span>';
            const textContainer = element.querySelector('.text-content');
            
            function type() {
                if (i < text.length) {
                    let char = text.charAt(i);
                    // Handle encoded newlines from JSON string
                    if (char === '\\' && text.charAt(i+1) === 'n') {
                        char = '<br>';
                        i++;
                    }
                    textContainer.innerHTML += char;
                    i++;
                    scrollToBottom();
                    setTimeout(type, speed);
                } else {
                    isTyping = false;
                    element.querySelector('.cursor-blink').remove();
                    renderPrompts(); 
                    if (callback) callback();
                }
            }
            type();
        }

        function scrollToBottom() {
            chatContainer.scrollTop = chatContainer.scrollHeight;
        }

        function resetChat() {
            if(isTyping) return;
            initChat();
        }

        function renderSkillsChart() {
            const ctx = document.getElementById('skillsChart');
            if (chartInstance) chartInstance.destroy();

            chartInstance = new Chart(ctx, {
                type: 'radar',
                data: {
                    labels: ['UX Design', 'Agile/Scrum', 'Journey Mapping', 'PRD Writing', 'A/B Testing', 'Data Analysis', 'Python/PyTorch'],
                    datasets: [{
                        label: 'Mức độ thông thạo',
                        data: [90, 85, 95, 80, 85, 80, 75],
                        fill: true,
                        backgroundColor: 'rgba(37, 99, 235, 0.2)',
                        borderColor: 'rgb(37, 99, 235)',
                        pointBackgroundColor: 'rgb(37, 99, 235)',
                        pointBorderColor: '#fff',
                        pointHoverBackgroundColor: '#fff',
                        pointHoverBorderColor: 'rgb(37, 99, 235)'
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    scales: {
                        r: {
                            angleLines: { color: 'rgba(0,0,0,0.1)' },
                            grid: { color: 'rgba(0,0,0,0.1)' },
                            pointLabels: { font: { size: 12, family: "'Inter', sans-serif", weight: '600' }, color: '#1e293b' },
                            ticks: { display: false, min: 0, max: 100, stepSize: 20 }
                        }
                    },
                    plugins: {
                        legend: { display: false },
                        tooltip: {
                            backgroundColor: 'rgba(30, 41, 59, 0.9)',
                            padding: 10,
                            callbacks: {
                                label: function(context) {
                                    let val = context.raw;
                                    if(val >= 90) return ' Rất Tốt';
                                    if(val >= 80) return ' Tốt';
                                    if(val >= 70) return ' Khá';
                                    return ' ' + val + '%';
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

# Gọi thành phần (component) để hiển thị toàn bộ giao diện lên Streamlit
components.html(html_code, height=850, scrolling=True)
