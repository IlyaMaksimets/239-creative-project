import '../styles/Form.css';
import {useState} from "react";
import url from "../utils";

export default function SignUpForm() {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [passwordConfirmation, setPasswordConfirmation] = useState("");
    return (
        <div className="formBox">
            <input className="textInput" onChange={(e) => setUsername(e.target.value)}/>
            <input className="textInput" onChange={(e) => setPassword(e.target.value)}/>
            <input className="textInput" onChange={(e) => setPasswordConfirmation(e.target.value)}/>
            <button className="submit" onClick={() => fetch(url("/register"), {
                method: "POST",
                body: JSON.stringify({
                    username: username,
                    password: password,
                    passwordConfirmation: passwordConfirmation
                }),
                headers: {'Content-Type': 'application/json'},
                credentials: "include"
            }).then((response) => {
                if (response.status === 200) {
                    window.location.replace("/cp/home")
                }
            })}>Submit
            </button>
        </div>
    );
}
