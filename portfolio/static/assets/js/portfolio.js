// my_page.js
document.addEventListener('DOMContentLoaded', function () {
    const appContainer = document.getElementById('portfolio');
  
    // Function to load content into the app container
    function loadContent(content) {
      appContainer.innerHTML = content;
    }
  
    // Event listener for clicks on links
    document.addEventListener('click', function (event) {
      const target = event.target;
  
      // Check if the clicked element is a link
      if (target.tagName === 'A' && target.getAttribute('href')) {
        // Prevent the default behavior of the link
        event.preventDefault();
  
        // Fetch the content of the link's href
        fetch(target.getAttribute('href'))
          .then(response => response.text())
          .then(content => {
            // Load the content into the app container
            loadContent(content);
  
            // Push the new URL to the browser's history
            history.pushState({}, '', target.getAttribute('href'));
          })
          .catch(error => {
            console.error('Error fetching content:', error);
          });
      }
    });
  
    // Handle back/forward browser navigation
    window.addEventListener('popstate', function (event) {
      // Fetch the content of the current URL
      fetch(window.location.href)
        .then(response => response.text())
        .then(content => {
          // Load the content into the app container
          loadContent(content);
        })
        .catch(error => {
          console.error('Error fetching content:', error);
        });
    });
  });
  