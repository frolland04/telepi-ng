// *** code.js ***
// Ici c'est la place du code Javascript!

function view(s)
{
    // Async. HTTP depuis le Javascript...
    var httpReq = new XMLHttpRequest();

    httpReq.onreadystatechange = function()
    {
        if (httpReq.readyState == 4 && httpReq.status == 200)
        {
            view_div.innerHTML = httpReq.responseText;
        }
        else
        {
            view_div.innerHTML = "..."
        }
    };

    httpReq.open("GET", s, true);
    httpReq.send(null);
}