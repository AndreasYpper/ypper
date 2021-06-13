import { reactive } from 'vue'
import axios from 'axios'

const user = reactive({
    first_name: '',
    last_name: '',
    email: '',
    phone: '',
    admin: false,
    authenticated: false,
    authentication_failed: false
})

function setUser(fname, lname, email, phone, admin, authenticated) {
    user.first_name = fname
    user.last_name = lname
    user.email = email
    user.phone = phone
    user.admin = admin
    user.authenticated = authenticated
    user.authentication_failed = false
}

function check_cookie_name(name) {
    var match = document.cookie.match(
        new RegExp("(^| )" + name + "=([^;]+)")
    );
    if (match) {
        return match[2];
    } else {
        //  console.log('--something went wrong---');
    }
}

function logout() {
    user.first_name = ''
    user.last_name = ''
    user.email = ''
    user.phone = ''
    user.admin = false
    user.authenticated = false
    user.authentication_failed = false
}

function getUser() {
    if (user.authenticated) {
        return user
    }

    if (user.authentication_failed) {
        return user
    }

    const fetchUser = () => {
        var cookie = check_cookie_name("csrf_access_token");
        axios.get(process.env.VUE_APP_API_URL + 'profile',
            {
                headers: {
                    "X-CSRF-TOKEN": cookie, "Content-Type": "application/json"
                },
                withCredentials: true
            })
            .then((response) => {
                setUser(response.data.first_name, response.data.last_name, response.data.email, response.data.phone, false, true)
            })
            .catch((error) => {
                if (error) {
                    user.authentication_failed = true
                }
            })

        return user
    }

    var currUser = fetchUser()

    return currUser
}

export default { setUser, getUser, logout }