document.addEventListener('DOMContentLoaded', () => {
    const searchButton = document.getElementById('search-button');
    const searchInput = document.getElementById('search-input');
    const resultsOutput = document.getElementById('results-output');
    const textbookList = document.getElementById('textbook-list');

    // Fetch and display the list of textbooks
    fetch('/textbooks')
        .then(response => response.json())
        .then(data => {
            if (data.textbooks) {
                data.textbooks.forEach(book => {
                    const li = document.createElement('li');
                    li.textContent = book;
                    textbookList.appendChild(li);
                });
            }
        })
        .catch(error => console.error('Error fetching textbooks:', error));

    const performSearch = () => {
        const query = searchInput.value;
        if (!query) return;

        resultsOutput.textContent = 'Searching...';

        fetch(`/search?query=${encodeURIComponent(query)}`)
            .then(response => response.json())
            .then(data => {
                console.log("Search results from backend:", data); // For debugging

                if (data.error) {
                    resultsOutput.textContent = `Error: ${data.error}`;
                } else if (data.results && data.results.length > 0) {
                    // For debugging, display the raw JSON data to understand its structure.
                    let resultText = data.results[0];
                    // Handle markdown-style bolding and newlines
                    resultText = resultText.replace(/^### (.*$)/gim, '<h3>$1</h3>');
                    resultText = resultText.replace(/\*\*(.*?)\*\*/g, '<b>$1</b>');
                    resultText = resultText.replace(/\n/g, '<br>');
                    resultsOutput.innerHTML = resultText;
                    renderMathInElement(resultsOutput, {
                        delimiters: [
                            {left: "$$", right: "$$", display: true},
                            {left: "\\[", right: "\\]", display: true},
                            {left: "\\(", right: "\\)", display: false},
                            {left: "$", right: "$", display: false}
                        ]
                    });
                } else {
                    resultsOutput.textContent = 'No results found.';
                }
            })
            .catch(error => {
                resultsOutput.textContent = `Error: ${error}`;
                console.error('Error during search:', error);
            });
    };

    searchButton.addEventListener('click', performSearch);
    searchInput.addEventListener('keypress', (event) => {
        if (event.key === 'Enter') {
            performSearch();
        }
    });
});
