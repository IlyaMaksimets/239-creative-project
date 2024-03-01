import '../styles/LoginPage.css';
import LoginForm from "../elements/LoginForm";
import url from "../utils";

export default function LoginPage() {
    fetch(url("/"), {method: "GET", credentials: "include"}).then((response) => {
        if (response.status === 200){
            window.location.replace("http://localhost:3000/home")
        }
    });
    return (
        <>
            <h1 className="LoginTitle">Login</h1>
            <LoginForm/>
        </>
    );
}
