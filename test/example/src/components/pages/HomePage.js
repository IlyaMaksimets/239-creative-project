import '../styles/MainHomePage.css';
import {Outlet, useNavigate} from 'react-router-dom';

export default function HomePage() {
    const navigate = useNavigate();
    return (
        <body>
        <div>
            <h1 className="gameTitle">Grand Battle</h1>
            <button className="profileButton" onClick={() => navigate('profile', {replace: false})}>Profile</button>
            <button className="installButton" onClick={() => {
                window.location.href = 'https://github.com/IlyaMaksimets/239-creative-project';
            }}>Install now</button>
            <button className="logoutButton" onClick={() => navigate('logout', {replace: false})}>Logout</button>
            <p className="versionP">v.0.0.1</p>
            <Outlet/>
        </div>
        </body>
    );
}
