import '../styles/LogoutPage.css';
import '../styles/MainHomePage.css'
import url from "../utils";

export default function LoginPage() {
    fetch(url("/"), {method: "GET", credentials: "include"}).then((response) => {
        if (response.status !== 200){
            window.location.replace("/")
        }
    });

    return (
        <>
            <h1 className="LogoutTitle">Are you sure you wanna end current session?</h1>
            <div>
                <button className="logoutButtonYes" onClick={() => {
                    fetch(url('/logout'), {method: "POST", credentials: "include"}).then(() => window.location.replace("/"))
                }}>Yes</button>
                <button className="logoutButtonNo" onClick={() => window.location.replace("/home")}>No</button>
            </div>
        </>
    );
}
