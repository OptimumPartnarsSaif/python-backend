<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Farm Fresh To-Do List</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Luckiest+Guy&family=Inter:wght@400;600&display=swap');
        body {
            font-family: 'Inter', sans-serif;
            background-color: #d1e7c4; /* Light green farm field color */
            background-image: url('https://placehold.co/1920x1080/c3d9b8/ffffff?text=');
            background-size: cover;
            background-repeat: no-repeat;
            background-position: center;
        }
        .container {
            max-width: 600px;
        }
        .card {
            background-color: #fefcf2; /* Creamy farm house color */
            border-radius: 2rem;
            box-shadow: 0 15px 25px -5px rgba(0, 0, 0, 0.2);
            border: 4px solid #a3b890;
        }
        .header-font {
            font-family: 'Luckiest Guy', cursive;
            color: #556b2f; /* Dark farm green */
            letter-spacing: 2px;
            text-shadow: 2px 2px 0px #fff, 4px 4px 0px #a3b890;
        }
        .input-container {
            background-color: #f0f4e4;
            border-radius: 1.5rem;
            padding: 0.75rem;
        }
        .grocery-list {
            list-style: none;
            padding: 0;
            margin: 0;
        }
        .list-item {
            display: flex;
            align-items: center;
            justify-content: space-between;
            background-color: #ffffff;
            border: 2px solid #a3b890;
            border-radius: 1.25rem;
            margin-bottom: 1rem;
            padding: 1rem 1.5rem;
            transition: all 0.3s ease;
            transform: scale(1);
            animation: fadeIn 0.5s ease-out;
            cursor: pointer;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
        }
        .list-item:hover {
            transform: scale(1.03) translateY(-3px);
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
        }
        .list-item.removed {
            animation: fadeOut 0.5s ease-in forwards;
        }
        .list-item.completed .item-text {
            text-decoration: line-through;
            color: #9ca3af;
        }
        .delete-btn {
            background-color: #e57373; /* Red fruit color */
            color: #ffffff;
            border: none;
            border-radius: 50%;
            width: 2.5rem;
            height: 2.5rem;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.5rem;
            font-weight: bold;
            transition: background-color 0.2s, transform 0.2s;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
        }
        .delete-btn:hover {
            background-color: #d32f2f;
            transform: rotate(15deg);
        }
        .add-btn {
            background-color: #4CAF50; /* Fresh green color */
            color: #ffffff;
            border-radius: 1.25rem;
            padding: 0.75rem 2rem;
            font-weight: 600;
            transition: background-color 0.2s, transform 0.2s;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        }
        .add-btn:hover {
            background-color: #388e3c;
            transform: translateY(-2px);
        }
        
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(-20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        @keyframes fadeOut {
            from { opacity: 1; transform: scale(1); }
            to { opacity: 0; transform: scale(0.8); height: 0; margin-bottom: 0; padding-top: 0; padding-bottom: 0; border: none; }
        }
        @keyframes float {
            0% { transform: translateY(0px); }
            50% { transform: translateY(-5px); }
            100% { transform: translateY(0px); }
        }
        .list-item {
            animation: fadeIn 0.5s ease-out, float 3s ease-in-out infinite;
        }
    </style>
</head>
<body class="bg-gray-100 min-h-screen flex items-center justify-center py-10">

    <div class="container mx-auto px-4">
        <div class="card p-10">
            <h1 class="header-font text-5xl text-center mb-8">My Farm List</h1>
            
            <div class="input-container flex items-center mb-8">
                <input type="text" id="itemInput" placeholder="Add fresh produce..." class="flex-1 bg-white border border-gray-300 rounded-lg py-3 px-4 focus:outline-none focus:ring-2 focus:ring-green-600 focus:border-transparent transition duration-200 ease-in-out">
                <button id="addItemBtn" class="add-btn ml-4">Grow Item</button>
            </div>

            <ul id="groceryList" class="grocery-list">
                <!-- List items will be added here dynamically -->
            </ul>
        </div>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', () => {
            const itemInput = document.getElementById('itemInput');
            const addItemBtn = document.getElementById('addItemBtn');
            const groceryList = document.getElementById('groceryList');

            // Function to create a new list item
            function createListItem(text) {
                const li = document.createElement('li');
                li.className = 'list-item';
                li.innerHTML = `
                    <span class="item-text text-lg font-medium text-gray-700 flex-1">${text}</span>
                    <button class="delete-btn">&times;</button>
                `;
                return li;
            }

            // Add item to the list
            function addItem() {
                const itemText = itemInput.value.trim();
                if (itemText !== '') {
                    const newItem = createListItem(itemText);
                    groceryList.appendChild(newItem);
                    itemInput.value = ''; // Clear the input field
                }
            }

            // Handle adding item on button click or Enter key
            addItemBtn.addEventListener('click', addItem);
            itemInput.addEventListener('keydown', (e) => {
                if (e.key === 'Enter') {
                    addItem();
                }
            });

            // Handle removing and marking as completed
            groceryList.addEventListener('click', (e) => {
                const target = e.target;
                const listItem = target.closest('.list-item');

                if (!listItem) return; // Exit if the click wasn't on a list item

                if (target.classList.contains('delete-btn')) {
                    // Remove item
                    listItem.classList.add('removed');
                    listItem.addEventListener('animationend', () => {
                        listItem.remove();
                    });
                } else {
                    // Mark as completed
                    listItem.classList.toggle('completed');
                }
            });
            
            // Initial items for demonstration
            const initialItems = ['Carrots', 'Potatoes', 'Cabbage'];
            initialItems.forEach(item => {
                groceryList.appendChild(createListItem(item));
            });
        });
    </script>
</body>
</html>
