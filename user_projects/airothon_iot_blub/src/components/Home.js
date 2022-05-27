import React from 'react';
import './Home.css'

function Home(props) {
    const bulb_on =()=>{
        document.getElementById('bulb').src='https://i.postimg.cc/6QyTynzr/bulb-on.png';
    }
    const bulb_off =()=>{
        document.getElementById('bulb').src='https://i.postimg.cc/KjK1wL3c/bulb-off.png';
    }
    return (
        <div>
            <header>
                <h1>IOT project:- Bulb on/off</h1>
            </header>
            <section>
                <img src="https://i.postimg.cc/KjK1wL3c/bulb-off.png" id="bulb" style={{width:"200px"}}/>
                <div class="btn_container"><button id="on" class="bulb_btn" onClick={bulb_on}>on</button>
                <button id="off" class="bulb_btn" onClick={bulb_off}>off</button></div>
                <h3 style={{marginTop:"3vh"}}>Status: No Device detected!!. Please connect yout iot device with bulb for demonstration</h3>
            </section>
        </div>
    );
}

export default Home;