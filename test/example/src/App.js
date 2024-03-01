import './App.css';
import MainPage from "./components/pages/MainPage";
import HomePage from "./components/pages/HomePage";
import LoginPage from "./components/pages/LoginPage";
import SignUpPage from "./components/pages/SignUpPage";
import LogoutPage from "./components/pages/LogoutPage";
import ProfilePage from "./components/pages/ProfilePage";
import {BrowserRouter, Routes, Route} from "react-router-dom";

function App() {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<MainPage />}/>
                <Route path="/home" element={<HomePage />}/>
                <Route path="/login" element={<LoginPage />} />
                <Route path="/register" element={<SignUpPage />} />
                <Route path="/home/logout" element={<LogoutPage />} />
                <Route path="/home/profile" element={<ProfilePage />} />
            </Routes>
        </BrowserRouter>
    );
}
export default App;
