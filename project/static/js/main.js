makeRequest();
    function updateRequestUrl(url) {
        document.getElementById('request-url-input').value = url;
        makeRequest();
    }
    function makeRequest() {
        var url = document.getElementById('request-url-input').value;
        const proxyurl = "https://cors-anywhere.herokuapp.com/";
        var request = new XMLHttpRequest();
        request.onreadystatechange = function() {
            if (request.readyState == XMLHttpRequest.DONE) {
                if (request.status == 200) {
                    var jsonData = JSON.parse(request.responseText);
                    document.getElementById('response-output').innerHTML = JSON.stringify(jsonData, null, '\t');
                } else if (request.status == 404) {
                    document.getElementById('response-output').innerHTML =
                        'Could not find any resource that matches the request, try again!';
                } else {
                    document.getElementById('response-output').innerHTML =
                        'Somethin went wrong. If this keeps happening, please post an issue at: https://github.com/joakimskoog/AnApiOfIceAndFire/issues';
                }
            }
        };
        request.open('GET', proxyurl+url);
        request.send();
    }