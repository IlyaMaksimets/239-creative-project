import '../styles/SignUpPage.css';
import SignUpForm from "../elements/SignUpForm";
import url from "../utils";

export default function SignUpPage() {
    fetch(url("/"), {method: "GET", credentials: "include"}).then((response) => {
        if (response.status === 200){
            window.location.replace("/home")
        }
    });

    return (<>
            <h1 className="SignUpTitle">Sign Up</h1>
            <SignUpForm/>
        </>
    );
}
