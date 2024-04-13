import '../styles/MainHomePage.css';
import {Outlet, useNavigate} from 'react-router-dom';
import url from '../utils';

export default function MainPage() {
    const navigate = useNavigate();
    fetch(url("/"), {method: "GET", credentials: "include"}).then((response) => {
        if (response.status === 200){
            window.location.replace("/cp/home")
        }
    });
    return (
        <body>
        <div>
            <h1 className="gameTitle">Grand Battle</h1>
            <button className="installButton" onClick={() => {
                window.location.href = 'https://github.com/IlyaMaksimets/239-creative-project';
            }}>Install now</button>
            <button className="loginButton" onClick={() => navigate('login', {replace: false})}>Login</button>
            <button className="signUpButton" onClick={() => navigate('register', {replace: false})}>Sign up</button>
            <p className="versionP">v.0.0.1</p>
            <Outlet/>
        </div>
        </body>
    );
}
    