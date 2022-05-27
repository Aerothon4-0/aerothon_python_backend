import React, { useState,useEffect } from 'react';
import './Home.css'
import axios from "axios";

function Home(props) {
    const [bulbStatus,setBulbStatus] = useState(true)
    let PORT = parseInt(window.location.port)+2000
    // let PORT = 5003
    const get_bulb_status = async () => {
                console.log("before get api call")
                console.log(`http://0.0.0.0:${PORT}/iot/buld`)
               // axios.get(`http://ec2-35-83-83-107.us-west-2.compute.amazonaws.com:${PORT}/user/get_data`)
               axios.get(`http://0.0.0.0:${PORT}/iot/buld`)
               .then(function (response) {
                   // After fetching data stored it in posts state.
                    console.log(response)
                    console.log(response.data.response_data.bulb_status)
                    setBulbStatus(response.data.response_data.bulb_status);
                    if(response.data.response_data.bulb_status==true){
                        bulb_on();
                    }
                    else{
                        bulb_off();
                    }
               })
               .catch(function (error) {
                    console.log(error);
               });
           }
    const save_bulb_status = async (bulbStatus) => {
                var obj={"bulb_status" : bulbStatus }
                console.log("before api call")
                console.log(`http://0.0.0.0:${PORT}/user/get_data`)
                console.log(obj)
               // axios.get(`http://ec2-35-83-83-107.us-west-2.compute.amazonaws.com:${PORT}/user/get_data`)
                axios.post(`http://0.0.0.0:${PORT}/iot/buld`, obj)
               .then(function (response) {
                   // After fetching data stored it in posts state.
                    console.log(response)
               })
               .catch(function (error) {
                    console.log(error);
               });
           }
    const bulb_on =()=>{
        console.log("start")
        setBulbStatus(true);
        document.getElementById('bulb').src='https://i.postimg.cc/6QyTynzr/bulb-on.png';
        save_bulb_status(true);
    }
    const bulb_off =()=>{
        setBulbStatus(false);
        document.getElementById('bulb').src='https://i.postimg.cc/KjK1wL3c/bulb-off.png';
        save_bulb_status(false);
    }
    useEffect(() => {
        get_bulb_status();
    }, []);
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