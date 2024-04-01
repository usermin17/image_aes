
        function displayImage() {
            // Get the input value (image path)
            var imagePath = document.getElementById('imagePath').value;
            
            // Get the image container element
            var imageContainer = document.getElementById('imageContainer');
            
            // Create an <img> element
            var imageElement = document.createElement('img');
            
            // Set the src attribute of the <img> element to the image path
            imageElement.src = imagePath;
            
            // Append the <img> element to the image container
            imageContainer.appendChild(imageElement);
        }
