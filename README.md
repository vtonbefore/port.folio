<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MARION JEPKORIR | SOFTWARE Developer & Student</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        /* Global Styles */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Poppins', sans-serif;
        }
        
        :root {
            --primary-color: #3498db;
            --secondary-color: #2c3e50;
            --light-color: #ecf0f1;
            --dark-color: #2c3e50;
            --accent-color: #e74c3c;
        }
        
        html {
            scroll-behavior: smooth;
        }
        
        body {
            background-color: var(--light-color);
            color: var(--dark-color);
            line-height: 1.6;
        }
        
        a {
            text-decoration: none;
            color: var(--primary-color);
        }
        
        .container {
            width: 90%;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px 0;
        }
        
        section {
            padding: 60px 0;
        }
        
        .section-title {
            text-align: center;
            margin-bottom: 40px;
            font-size: 2.5rem;
            color: var(--secondary-color);
            position: relative;
        }
        
        .section-title::after {
            content: '';
            position: absolute;
            bottom: -10px;
            left: 50%;
            transform: translateX(-50%);
            width: 80px;
            height: 4px;
            background-color: var(--primary-color);
        }
        
        .btn {
            display: inline-block;
            padding: 10px 20px;
            background-color: var(--primary-color);
            color: white;
            border-radius: 5px;
            transition: all 0.3s ease;
            border: none;
            cursor: pointer;
        }
        
        .btn:hover {
            background-color: var(--secondary-color);
            transform: translateY(-3px);
        }
        
        /* Header Styles */
        header {
            background-color: var(--secondary-color);
            color: white;
            padding: 20px 0;
            position: fixed;
            width: 100%;
            top: 0;
            z-index: 1000;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }
        
        .header-container {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        
        .logo {
            font-size: 1.8rem;
            font-weight: 700;
        }
        
        .logo span {
            color: var(--primary-color);
        }
        
        nav ul {
            display: flex;
            list-style: none;
        }
        
        nav ul li {
            margin-left: 30px;
        }
        
        nav ul li a {
            color: white;
            font-weight: 500;
            transition: color 0.3s ease;
        }
        
        nav ul li a:hover {
            color: var(--primary-color);
        }
        
        .menu-toggle {
            display: none;
            cursor: pointer;
            font-size: 1.5rem;
        }
        
        /* Hero Section */
        #hero {
            height: 100vh;
            display: flex;
            align-items: center;
            background: linear-gradient(rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.7)), url('https://images.unsplash.com/photo-1499750310107-5fef28a66643?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1470&q=80') no-repeat center center/cover;
            color: white;
            text-align: center;
        }
        
        .hero-content {
            max-width: 800px;
            margin: 0 auto;
        }
        
        .hero-content h1 {
            font-size: 3.5rem;
            margin-bottom: 20px;
            animation: fadeInDown 1s ease;
        }
        
        .hero-content p {
            font-size: 1.2rem;
            margin-bottom: 30px;
            animation: fadeInUp 1s ease;
        }
        
        .hero-content .btn {
            animation: fadeIn 1.5s ease;
        
        }
        .cv-section {
    text-align: center;
    margin-top: 50px;
}

.cv-button {
    display: inline-block;
    padding: 12px 20px;
    font-size: 18px;
    color: white;
    background-color: #0b141f; /* Dark blue */
    text-decoration: none;
    border-radius: 5px;
    transition: background 0.3s ease-in-out;
}

.cv-button:hover {
    background-color: #09131f; /* Darker blue on hover */
}

        
        /* About Section */
        #about {
            background-color: white;
        }
        
        .about-content {
            display: flex;
            align-items: center;
            gap: 50px;
        }
        
        .about-img {
            flex: 1;
            border-radius: 10px;
            overflow: hidden;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
        }
        
        .about-img img {
            width: 100%;
            height: auto;
            display: block;
            transition: transform 0.5s ease;
        }
        
        .about-img:hover img {
            transform: scale(1.05);
        }
        .about-text {
            flex: 1;
        }
        
        .about-text h3 {
            font-size: 1.8rem;
            margin-bottom: 20px;
            color: var(--secondary-color);
        }
        
        .about-text p {
            margin-bottom: 15px;
        }
        
        .skills {
            margin-top: 30px;
        }
        
        .skill-item {
            margin-bottom: 20px;
        }
        
        .skill-name {
            display: flex;
            justify-content: space-between;
            margin-bottom: 5px;
        }
        
        .skill-bar {
            height: 10px;
            background-color: #ddd;
            border-radius: 5px;
            overflow: hidden;
        }
        
        .skill-progress {
            height: 100%;
            background-color: var(--primary-color);
            border-radius: 5px;
        }
        
        /* Project Section */
        /* Project Section Title */
.projects-title {
    font-size: 36px;
    font-weight: bold;
    text-align: center;
    margin-bottom: 20px;
    position: absolute;
    align-items: center;
}

/* Blue Underline */
.projects-title::after {
    content: "title";
    width: 70px;
    height: 4px;
    background-color: #172033;
    position: absolute;
    left: 50%;
    transform: translateX(-50%);
    bottom: -5px;
}

/* Project Grid Layout */
.projects-container {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 20px;
    width: 80%;
    max-width: 400px;
}

/* Project Box */
.project-box {
    background-color: white;
    border-radius: 10px;
    padding: 15px;
    text-align: center;
    position: relative;
    border: 2px solid black;
    box-shadow: 0px 0px 15px rgba(0, 0, 0, 0.2);
    transition: transform 0.3s ease-in-out;
}

/* Hover Effect */
.project-box:hover {
    transform: scale(1.05);
}

/* Hidden Checkbox for Toggle */
input[type="checkbox"] {
    display: none;
}

/* Project Title */
#project {
    background-color:white;
    padding: 20px;
    text-align: center;
    font-size: 2rem;
    color: #331b1b;
    margin-bottom: 20px;
    text-underline-position: below ;
}
.project info h2{
    font-size: 2rem;
    color: #fff;
    margin-bottom: 10px;
    align-items: center;
}

.project-title {
    text-align: center;
    font-size: 48px;
    font-weight: bold;
    text-transform: uppercase;
    position: relative;
    margin-bottom: 20px;
}

.project-title::after {
    content: "";
    display: block;
    width: 80px;
    height: 4px;
    background-color: #0056b3;
    margin: 10px auto;
}

.project-container {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-wrap: wrap;
    gap: 20px;
    padding: 20px;
}

.project-box {
    background: rgba(0, 0, 0, 0.8);
    color: white;
    width: 60%; /* Long width */
    height: 200px; /* Short height */
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
    border-radius: 10px;
    box-shadow: 0px 0px 10px #263d57; /* Lighting effect */
    transition: transform 0.3s ease-in-out;
}

.project-box:hover {
    transform: scale(1.05);
}


.project-title:hover {
    background-color: #333;
}

/* Project Content */
.project-content {
    background-color: #444;
    padding: 15px;
    display: none;
    border-radius: 0 0 10px 10px;
    position: relative;
    margin-top: 10px;
}

/* Triangle Dropdown Indicator */
.triangle {
    width: 0;
    height: 0;
    border-left: 15px solid transparent;
    border-right: 15px solid transparent;
    border-bottom: 15px solid #0055ff;
    position: absolute;
    top: -15px;
    left: 50%;
    transform: translateX(-50%);
}

/* View Button */
.view-btn {
    display: inline-block;
    margin-top: 10px;
    padding: 8px 15px;
    color: white;
    text-decoration: none;
    background-color: #0055ff;
    border-radius: 5px;
    transition: 0.3s;
}

.view-btn:hover {
    background-color: #0033aa;
}

/* Toggle Animation */
input[type="checkbox"]:checked + .project-title + .project-content {
    display: block;
    animation: fadeIn 0.5s ease-in-out;
}

/* Fade In Effect */
@keyframes fadeIn {
    from {
        opacity: 0;
        transform: translateY(-10px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

/* Responsive Design */
@media (max-width: 768px) {
    .projects-container {
        grid-template-columns: 1fr;
    }
}

        /* Contact Section */
        #contact {
            background-color: white;
        }
        
        .contact-container {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 40px;
        }
        
        .contact-info {
            margin-bottom: 30px;
        }
        
        .contact-info h3 {
            font-size: 1.5rem;
            margin-bottom: 20px;
            color: var(--secondary-color);
        }
        
        .contact-info p {
            margin-bottom: 15px;
        }
        
        .contact-info .info-item {
            display: flex;
            align-items: center;
            margin-bottom: 15px;
        }
        
        .contact-info .info-item i {
            width: 40px;
            height: 40px;
            background-color: var(--primary-color);
            color: white;
            border-radius: 50%;
            display: flex;
            justify-content: center;
            align-items: center;
            margin-right: 15px;
            font-size: 1.2rem;
        }
        
        .contact-form .form-group {
            margin-bottom: 20px;
        }
        
        .contact-form input,
        .contact-form textarea {
            width: 100%;
            padding: 12px 15px;
            border: 1px solid #ddd;
            border-radius: 5px;
            font-size: 1rem;
            transition: border-color 0.3s ease;
        }
        
        .contact-form input:focus,
        .contact-form textarea:focus {
            border-color: var(--primary-color);
            outline: none;
        }
        
        .contact-form textarea {
            resize: vertical;
            min-height: 150px;
        }
        
        /* Footer */
        footer {
            background-color: var(--secondary-color);
            color: white;
            text-align: center;
            padding: 30px 0;
        }
        
        .social-links {
            display: flex;
            justify-content: center;
            margin-bottom: 20px;
        }
        
        .social-links a {
            display: flex;
            justify-content: center;
            align-items: center;
            width: 40px;
            height: 40px;
            background-color: rgba(255, 255, 255, 0.1);
            color: white;
            border-radius: 50%;
            margin: 0 10px;
            transition: all 0.3s ease;
        }
        
        .social-links a:hover {
            background-color: var(--primary-color);
            transform: translateY(-5px);
        }
        
        /* Animations */
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
        
        @keyframes fadeInDown {
            from {
                opacity: 0;
                transform: translateY(-20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        /* Responsive Styles */
        @media (max-width: 992px) {
            .about-content {
                flex-direction: column;
            }
            
            .about-img, .about-text {
                flex: none;
                width: 100%;
            }
        }
        
        @media (max-width: 768px) {
            .menu-toggle {
                display: block;
            }
            
            nav {
                position: absolute;
                top: 100%;
                left: 0;
                width: 100%;
                background-color: var(--secondary-color);
                padding: 20px;
                box-shadow: 0 5px 10px rgba(0, 0, 0, 0.1);
                clip-path: circle(0% at 100% 0);
                transition: clip-path 0.5s ease;
            }
            
            nav.active {
                clip-path: circle(150% at 100% 0);
            }
            
            nav ul {
                flex-direction: column;
            }
            
            nav ul li {
                margin: 10px 0;
            }
            
            .hero-content h1 {
                font-size: 2.5rem;
            }
            
            .section-title {
                font-size: 2rem;
            }
        }
        
        @media (max-width: 576px) {
            .hero-content h1 {
                font-size: 2rem;
            }
            
            .portfolio-grid {
                grid-template-columns: 1fr;
            }
        }
        /* Full-width and extended footer */
.footer {
    width: 100vw; /* Full viewport width */
    height: 200px; /* Adjust height as needed */
    background-color: #111; /* Dark footer background */
    color: white;
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
    padding: 20px;
    box-sizing: border-box;
}

/* Footer text styling */
.footer p {
    font-size: 18px;
    max-width: 800px;
    line-height: 1.6;
}

    </style>
</head>
<body>
    <!-- Header -->
    <header>
        <div class="container header-container">
            <div class="logo">Marion<span>Jepkorir</span></div>
            <div class="menu-toggle">
                <i class="fas fa-bars"></i>
            </div>
            <nav>
                <ul>
                    <li><a href="#hero">Home</a></li>
                    <li><a href="#about">About</a></li>
                    <li><a href="#projects">Projects</a></li>
                    <li><a href="#contact">Contact</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <!-- Hero Section -->
    <section id="hero">
        <div class="container">
            <div class="hero-content">
                <h1>Hello, I'm Marion Jepkorir </h1>
                <p>I am a passionate software developer with a keen interest in AI,machine learning and innovative tech solutions.Whether it's building intelligent systems or crafting wed experiences, I am always eager to learn and innovate.</p>
                <a href="#projects" class="btn">View My Projects</a>
            </div>
        </div>
    </section>
    <section class="cv-section">
        <h2>Download My CV</h2>
        <a href="c:\Users\HP\AppData\Roaming\Microsoft\Windows\Network Shortcuts\cv.pdf" download class="cv-button">Download CV</a>
    </section>
    

    <!-- About Section -->
    <section id="about">
        <div class="container">
            <h2 class="section-title">About Me</h2>
            <div class="about-content">
                <div class="about-img">
                    <img src="c:\Users\HP\Downloads\pexels-joshsorenson-1714208.jpg" alt="image of tech" width="400" height="1000">
                </div>
                <div class="about-text">
                    <h3>SOFTWARE DEVELOPER</h3>
                    <p>I am a software developer with a deep passion for machine learning and artificial intelligence.My approach to technology is rooted in innovation, problem-solving and creating solution that stand out.</p>
                    <p>I believe in building unique, impactful projects that push the boundaries of what's possible.whether it's software development or AI applications, i focus on combining creativity with techinal expertise to develop solutions that are both practical and forward-thinking.</p>
                    
                    <div class="skills">
                        <div class="skill-item">
                            <div class="skill-name">
                                <span>HTML/CSS</span>
                                <span>95%</span>
                            </div>
                            <div class="skill-bar">
                                <div class="skill-progress" style="width: 95%"></div>
                            </div>
                        </div>
                        <div class="skill-item">
                            <div class="skill-name">
                                <span>DATABASE</span>
                                <span>80%</span>
                            </div>
                            <div class="skill-bar">
                                <div class="skill-progress" style="width: 80%"></div>
                            </div>
                        </div>
                        <div class="skill-item">
                            <div class="skill-name">
                                <span>MACHINE LEARNING</span>
                                <span>87%</span>
                            </div>
                            <div class="skill-bar">
                                <div class="skill-progress" style="width: 87%"></div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Project Section -->
    <section id="projects">
        <div class="container">
        <h2 class="section-title">My Projects</h2>
    
        <div class="filter-buttons">
            <button class="filter-btn active"></button>
            <button class="filter-btn">Software Development</button>
            
        </div>
    
        <div class="projects-grid">
            <div class="project-box">
                <h3>Project 1</h3>
                <p>Web development project description.</p>
                <a href="https://github.com/vtonbefore/my-index.html--project.git" class="project-btn" target="_blank">View My Project</a>
            </div>
    
            <div class="project-box">
                <h3>Project 2</h3>
                <p>Python project description.</p>
                <a href="https://github.com/vtonbefore/python.calculator.git" class="project-btn" target="_blank">View My Project</a>
            </div>
    
            <div class="project-box">
                <h3>Project 3</h3>
                <p>Another web development project.</p>
                <a href="https://github.com/vtonbefore/index.html.git" class="project-btn" target="_blank">View My Project</a>
            </div>
        </div>
    </section>
    

    <!-- Contact Section -->
    <section id="contact">
        <div class="container">
            <h2 class="section-title">Contact Me</h2>
            <div class="contact-container">
                <div class="contact-info">
                    <h3>Get In Touch</h3>
                    <p>Feel free to reach out f or just a friendly hello!</p>
        
                    <div class="info-item">
                        <i class="fas fa-envelope"></i>
                        <span>beforevton@gmail.com</span>
                    </div>
                    <div class="info-item">
                        <i class="fas fa-phone"></i>
                        <span>+2457 96 244 335</span>
                    </div>
                    
                    <div class="social-links">
                        <a href="#"><i class="fab fa-github"></i></a>
                        <a href="#"><i class="fab fa-facebook-f"></i></a>
                        <a href="#"><i class="fab fa-instagram"></i></a>
                        <a href="#"><i class="fab fa-linkedin-in"></i></a>
                        
                    </div>
                </div>
                <div class="contact-form">
                    <form>
                        <div class="form-group">
                            <input type="text" placeholder="Your Name" required>
                        </div>
                        <div class="form-group">
                            <input type="email" placeholder="Your Email" required>
                        </div>
                        <div class="form-group">
                            <input type="text" placeholder="Subject">
                        </div>
                        <div class="form-group">
                            <textarea placeholder="Your Message" required></textarea>
                        </div>
                        <button type="submit" class="btn">Send Message</button>
                    </form>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer>
        <div class="container">
            <p>&copy; 2025 Marion Jepkorir. All Rights Reserved.</p>
        </div>
    </footer>

</body>
<html>
     <script>
    // Contact form submission
document.getElementById("contactForm").addEventListener("submit", function (event) {
    event.preventDefault(); // Prevent page reload

    let formData = {
        name: document.getElementById("name").value,
        email: document.getElementById("email").value,
        subject: document.getElementById("subject").value,
        message: document.getElementById("message").value
    };

    fetch("http://localhost:3000/submit", { // Change URL if hosting online
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(formData)
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("response").innerHTML = data.message; // Show response message
    })
    .catch(error => console.error("Error:", error));
});
        /* JavaScript for Menu Toggle */
        const menuToggle = document.querySelector('.menu-toggle');
        const nav = document.querySelector('nav');

        menuToggle.addEventListener('click', () => {
            nav.classList.toggle('active');
        });
    </script>
