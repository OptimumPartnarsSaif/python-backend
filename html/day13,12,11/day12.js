 <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>3D Division Calculator</title>
        <script src="https://cdn.tailwindcss.com"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Share+Tech+Mono&display=swap');
            
            body {
                font-family: 'Share Tech Mono', monospace;
                background-color: #000;
                color: #ffffff;
                overflow: hidden; /* Prevent scrollbars from 3D canvas */
            }

            #threejs-container {
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                z-index: -1;
                opacity: 0.8;
                transition: opacity 1s;
            }

            .card {
                background-color: rgba(255, 255, 255, 0.05);
                backdrop-filter: blur(10px);
                border: 1px solid rgba(255, 255, 255, 0.1);
                border-radius: 1.5rem;
                box-shadow: 0 4px 30px rgba(0, 0, 0, 0.5);
            }

            .header-font {
                font-family: 'Orbitron', sans-serif;
                color: #e0f2fe; /* Light blue for futuristic feel */
                text-shadow: 0 0 15px #ff00bf, 0 0 20px #ff0095;
            }
            
            .code-block {
                background-color: rgba(0, 0, 0, 0.2);
                border: 1px solid rgba(255, 255, 255, 0.15);
                border-radius: 0.75rem;
            }
            
            .result-box {
                background-color: rgba(67, 160, 71, 0.2);
                border: 1px solid #43a047;
                color: #a5d6a7;
                animation: glowing 1.5s infinite alternate;
            }
            .error-box {
                background-color: rgba(229, 57, 53, 0.2);
                border: 1px solid #e53935;
                color: #ef9a9a;
            }
            .button {
                background-color: #00bcd4;
                color: #1a1a1a;
                border-radius: 0.75rem;
                transition: background-color 0.2s, transform 0.2s, box-shadow 0.3s ease;
                text-shadow: none;
            }
            .button:hover {
                background-color: #00acc1;
                transform: scale(1.05);
                box-shadow: 0 0 15px #00e5ff;
            }

            input {
                background-color: rgba(255, 255, 255, 0.05);
                border: 1px solid rgba(255, 255, 255, 0.2);
                color: #e0f2fe;
                border-radius: 0.75rem;
                transition: box-shadow 0.3s ease;
            }
            input::placeholder {
                color: rgba(255, 255, 255, 0.4);
            }
            input:focus {
                box-shadow: 0 0 10px #00e5ff;
            }

            @keyframes glowing {
                from { box-shadow: 0 0 5px #43a047; }
                to { box-shadow: 0 0 20px #43a047; }
            }
        </style>
    </head>
    <body class="flex items-center justify-center min-h-screen p-8">

        <!-- Three.js Canvas Container -->
        <div id="threejs-container"></div>

        <div class="card p-8 w-full max-w-2xl relative z-10">
            <h1 class="header-font text-4xl text-center font-bold mb-6">Robust Division Function</h1>
            
            <p class="mb-6 text-center text-gray-400">Enter two numbers to see the result. The function handles division by zero elegantly.</p>

            <!-- Function Code Block -->
            <div class="code-block p-4 mb-6 rounded-md overflow-x-auto">
                <pre><code class="language-javascript">/**
    * Divides two numbers and handles the case of division by zero.
    * @param {number} dividend - The number to be divided.
    * @param {number} divisor - The number to divide by.
    * @returns {number|string} The result of the division, or an error message if the divisor is zero.
    */
    function divideNumbers(dividend, divisor) {
        // Check if the divisor is zero
        if (divisor === 0) {
            // Return a specific message for this error
            return "Error: Cannot divide by zero.";
        }
        // Perform the division
        return dividend / divisor;
    }</code></pre>
            </div>

            <div class="flex flex-col md:flex-row space-y-4 md:space-y-0 md:space-x-4 mb-6">
                <input type="number" id="dividendInput" placeholder="Dividend (e.g., 10)" class="flex-1 p-3 focus:outline-none focus:ring-2 focus:ring-cyan-400 transition duration-200">
                <input type="number" id="divisorInput" placeholder="Divisor (e.g., 2)" class="flex-1 p-3 focus:outline-none focus:ring-2 focus:ring-cyan-400 transition duration-200">
                <button id="calculateBtn" class="button px-6 py-3 font-bold whitespace-nowrap">Calculate</button>
            </div>

            <div id="resultOutput" class="p-4 rounded-md text-center font-bold">
                <!-- Result will be displayed here -->
            </div>

        </div>

        <script>
            document.addEventListener('DOMContentLoaded', () => {
                const dividendInput = document.getElementById('dividendInput');
                const divisorInput = document.getElementById('divisorInput');
                const calculateBtn = document.getElementById('calculateBtn');
                const resultOutput = document.getElementById('resultOutput');
                const container = document.getElementById('threejs-container');

                // --- Three.js Setup ---
                let scene, camera, renderer, particles;
                let mouseX = 0, mouseY = 0;
                let windowHalfX = window.innerWidth / 2;
                let windowHalfY = window.innerHeight / 2;
                const particleCount = 2000;

                function initThreeJS() {
                    // Scene
                    scene = new THREE.Scene();

                    // Camera
                    camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
                    camera.position.z = 5;

                    // Renderer
                    renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
                    renderer.setPixelRatio(window.devicePixelRatio);
                    renderer.setSize(window.innerWidth, window.innerHeight);
                    container.appendChild(renderer.domElement);
                    
                    // Create Particle System
                    const particleGeometry = new THREE.BufferGeometry();
                    const particleVertices = [];
                    for (let i = 0; i < particleCount; i++) {
                        const x = (Math.random() - 0.5) * 10;
                        const y = (Math.random() - 0.5) * 10;
                        const z = (Math.random() - 0.5) * 10;
                        particleVertices.push(x, y, z);
                    }
                    particleGeometry.setAttribute('position', new THREE.Float32BufferAttribute(particleVertices, 3));

                    const particleMaterial = new THREE.PointsMaterial({
                        color: 0x00e5ff,
                        size: 0.05,
                        transparent: true,
                        blending: THREE.AdditiveBlending,
                        sizeAttenuation: true
                    });

                    particles = new THREE.Points(particleGeometry, particleMaterial);
                    scene.add(particles);

                    // Event Listeners
                    document.addEventListener('mousemove', onDocumentMouseMove, false);
                    window.addEventListener('resize', onWindowResize, false);
                }

                function onDocumentMouseMove(event) {
                    mouseX = (event.clientX - windowHalfX) * 0.0005;
                    mouseY = (event.clientY - windowHalfY) * 0.0005;
                }

                function onWindowResize() {
                    windowHalfX = window.innerWidth / 2;
                    windowHalfY = window.innerHeight / 2;
                    camera.aspect = window.innerWidth / window.innerHeight;
                    camera.updateProjectionMatrix();
                    renderer.setSize(window.innerWidth, window.innerHeight);
                }

                // Animation Loop
                function animate() {
                    requestAnimationFrame(animate);

                    // Rotate the particle system
                    particles.rotation.x += 0.0005;
                    particles.rotation.y += 0.001;

                    // Move the particle system based on mouse
                    particles.position.x += (mouseX - particles.position.x) * 0.05;
                    particles.position.y += (-mouseY - particles.position.y) * 0.05;

                    // Make the particles pulse
                    const time = Date.now() * 0.0005;
                    const positions = particles.geometry.attributes.position.array;
                    for (let i = 0; i < particleCount * 3; i += 3) {
                        positions[i] += Math.sin(time + positions[i] * 0.5) * 0.005;
                        positions[i+1] += Math.cos(time + positions[i+1] * 0.5) * 0.005;
                    }
                    particles.geometry.attributes.position.needsUpdate = true;

                    renderer.render(scene, camera);
                }

                
            function divideNumbers(dividend, divisor) {
        try {
        
            if (typeof dividend !== 'number' || typeof divisor !== 'number') {
                throw new Error("Invalid input: Both dividend and divisor must be numbers.");
            }

        
            if (divisor === 0) {
                throw new Error("Cannot divide by zero.");
            }

        
            return dividend / divisor;

        } catch (error) {
    
            return `Error: ${error.message}`;
        }
    }


                calculateBtn.addEventListener('click', () => {
                    const dividend = parseFloat(dividendInput.value);
                    const divisor = parseFloat(divisorInput.value);

                    if (isNaN(dividend) || isNaN(divisor)) {
                        resultOutput.className = "p-4 rounded-md text-center font-bold error-box";
                        resultOutput.textContent = "Please enter valid numbers.";
                        return;
                    }

                    const result = divideNumbers(dividend, divisor);

                    if (typeof result === 'string' && result.includes('Error')) {
                        resultOutput.className = "p-4 rounded-md text-center font-bold error-box";
                        resultOutput.textContent = result;
                    } else {
                        resultOutput.className = "p-4 rounded-md text-center font-bold result-box";
                        resultOutput.textContent = `Result: ${result}`;
                    }
                });

                // Start the 3D animation when the page loads
                window.onload = function () {
                    initThreeJS();
                    animate();
                };
            });
        </script>
    </body>
    </html>
