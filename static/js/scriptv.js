function previewMedia(input) {
    var previewContainer = document.getElementById('preview-container');
    var mediaPreview = document.querySelector('.previewDiv');
    
    // Remove any existing content in the preview container
    // previewContainer.innerHTML = '';

    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function(e) {
            var fileExtension = input.files[0].name.split('.').pop().toLowerCase();
            
            if (fileExtension === 'gif' || fileExtension === 'png' || fileExtension === 'jpeg' || fileExtension === 'jpg') {
                // Display image preview
                mediaPreview.innerHTML = '';
                var image = document.createElement('img');
                image.src = e.target.result;
                image.alt = 'Media Preview';
                mediaPreview.appendChild(image);
            } else if (fileExtension === 'mp4' || fileExtension === 'webm' || fileExtension === 'ogg') {
                // Display video preview
                // var video = document.createElement('video');
                previewContainer.src = e.target.result;
                previewContainer.controls = true;
                // video.poster = 'Media Preview';
                // previewContainer.appendChild(video);
            } else {
                // Unsupported file type
                console.error('Unsupported file type');
            }

            mediaPreview.style.display = 'block';
        };

        reader.readAsDataURL(input.files[0]);
    }
}
