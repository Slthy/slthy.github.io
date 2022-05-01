
const url = "https://pastebin.com/api/api_login.php"

const params = new URLSearchParams();
params.append('api_dev_key', 'P2evBxKN285xoolB4EEtTyifydbe91WD');
params.append('api_user_name', 'slthy');
params.append('api_user_password', 'bowcuf-8pasdU-digfoj');

fetch(url, {
    method: 'POST',
    headers: {'Content-Type': 'application/x-www-form-urlencoded', "mode": "no-cors"},
    body: params
}).then(res => {console.log(res)})