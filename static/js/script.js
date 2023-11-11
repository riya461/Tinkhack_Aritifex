function previewImage(input) {
    var preview = document.getElementById('preview');
    var imagePreview = document.querySelector('.previewDiv');

    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function(e) {
            preview.src = e.target.result;
            imagePreview.style.display = 'block';
        }

        reader.readAsDataURL(input.files[0]);
    }
}

function watchImageContentChange() {
    const outputImage = document.getElementById('output');
    const box3 = document.querySelector('.box3');
    const outputDiv = document.querySelector('.outputDiv');

    let currentImageContent = ''; // Store the current image content

    // Function to fetch the image content and compare it
    const checkImageContent = async () => {
        try {
            const response = await fetch(outputImage.src);
            const newImageContent = await response.blob();

            if (!currentImageContent) {
                currentImageContent = newImageContent;
            } else if (URL.createObjectURL(currentImageContent) !== URL.createObjectURL(newImageContent)) {
                // The image content has changed, so show the elements
                box3.style.display = 'block';
                outputDiv.style.display = 'block';

                // Update the currentImageContent for future comparisons
                currentImageContent = newImageContent;
            }
        } catch (error) {
            console.error('Error fetching image content:', error);
        }
    };

    // Periodically check for changes (e.g., every 5 seconds)
    const checkInterval = 5000; // 5 seconds
    setInterval(checkImageContent, checkInterval);

    // Initial check
    checkImageContent();
}

watchImageContentChange(); // Call the function to start watching for changes