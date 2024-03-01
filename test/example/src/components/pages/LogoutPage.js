import '../styles/LogoutPage.css';
import '../styles/MainHomePage.css'
import url from "../utils";

export default function LoginPage() {
    fetch(url("/"), {method: "GET", credentials: "include"}).then((response) => {
        if (response.status !== 200){
            window.location.replace("http://localhost:3000/")
        }
    });

    return (
        <>
            <h1 className="LogoutTitle">Are you sure you wanna end current session?</h1>
            <div>
                <button className="logoutButtonYes" onClick={() => {
                    fetch(url('/logout'), {method: "POST", credentials: "include"}).then(() => window.location.replace("http://localhost:3000/"))
                }}>Yes</button>
                <button className="logoutButtonNo" onClick={() => window.location.replace("http://localhost:3000/home")}>No</button>
            </div>
        </>
    );
}
