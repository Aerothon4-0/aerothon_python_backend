import React, { useState,useEffect } from 'react';
import './css/bootstrap.min.css'
import './css/style.css'
import './css/responsive.css'
import img1 from './images/logo.png'
import img2 from './images/box_img.png'
import img3 from './images/our_img1.jpg'
import img4 from './images/like.png'
import img5 from './images/comm.png'
import img6 from './images/our_img2.jpg'
import img7 from './images/like1.png'
import img8 from './images/comm1.png'
import Contact from './Contact'
import { useTranslation } from 'react-i18next';
import axios from "axios";

function Home(props) {
    const { t, i18n } = useTranslation();
    const [lang, setLang] = useState('en');
    const [cmpName,setCmpName] = useState("CompanyNameHere")
    const [blogName,setBlogName] = useState("BlogNameHere")
    const [des,setDes] = useState("some description")
    let PORT = parseInt(window.location.port)+2000
    console.log("PORT")
    console.log(PORT)
    useEffect(() => {
           const loadBlogName = async () => {
                console.log("before api call")
                console.log(`http://0.0.0.0:${PORT}/user/get_data`)
               // axios.get(`http://ec2-35-83-83-107.us-west-2.compute.amazonaws.com:${PORT}/user/get_data`)
               axios.get(`http://0.0.0.0:${PORT}/user/get_data`)
               .then(function (response) {
                   // After fetching data stored it in posts state.
                    console.log(response)
                    //console.log(response.data.response_data.website_name)
                    setBlogName(response.data.response_data.website_name);
                    setCmpName(response.data.response_data.company_name);
                    setDes(response.data.response_data.company_description)
               })
               .catch(function (error) {
                    console.log(error);
               });
           }
           // Call the function
           loadBlogName();
      }, []);

    function handleClick(){
        i18n.changeLanguage(document.getElementById('lang').value);
    }
    return (
        <div>
           <body class="main-layout">
                {/* <!-- header --> */}
                <header>
                    {/* <!-- header inner --> */}
                    <div  class="head_top">
                        <div class="header">
                        <div class="container-fluid">
                            <div class="row">
                                <div class="col-xl-3 col-lg-3 col-md-3 col-sm-3 col logo_section">
                                    <div class="full">
                                    <div class="center-desk">
                                        <div class="logo">
                                            <a href="index.html"><img src={img1} alt="#" /></a>
                                        </div>
                                    </div>
                                    </div>
                                </div>
                                <div class="col-xl-9 col-lg-9 col-md-9 col-sm-9">
                                    <nav class="navigation navbar navbar-expand-md navbar-dark ">
                                    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarsExample04" aria-controls="navbarsExample04" aria-expanded="false" aria-label="Toggle navigation">
                                    <span class="navbar-toggler-icon"></span>
                                    </button>
                                    <div class="collapse navbar-collapse" id="navbarsExample04">
                                        <ul class="navbar-nav mr-auto">
                                            <li class="nav-item">
                                                <a class="nav-link" href="#"> Home  </a>
                                            </li>
                                            <li class="nav-item">
                                                <a class="nav-link" href="#contact">About</a>
                                            </li>
                                            <li class="nav-item">
                                                <a class="nav-link" href="#">Contact</a>
                                            </li>
                                            <li class="nav-item" style={{display:"flex",flexDirection:"row",padding:0}}>
                                                <a class="nav-link" href="#">Lang-</a>
                                                <select name="lang" id="lang" style={{backgroundColor:"transparent",borderColor:"transparent",color:"white",textDecoration:"none",marginLeft:"-1.5vw"}} onChange={()=>handleClick('en')} defaultValue="en">
                                                    <option value="en" style={{color:"black",fontWeight:"bold"}} selected>eng</option>
                                                    <option value="hi" style={{color:"black",fontWeight:"bold"}} >hin</option>
                                                    <option value="chi" style={{color:"black",fontWeight:"bold"}} >chi</option>
                                                    <option value="sp" style={{color:"black",fontWeight:"bold"}} >spa</option>
                                                    </select>
                                            </li>
                                        </ul>
                                    </div>
                                    </nav>
                                </div>
                            </div>
                        </div>
                        </div>
                        {/* <!-- end header inner -->
                        <!-- end header -->
                        <!-- banner --> */}
                        <section class="banner_main">
                        <div class="container">
                            <div class="row d_flex">
                                <div class=" col-xl-8 col-lg-8 col-md-8 col-12-9">
                                    <div class="text-bg">
                                    <h1>{cmpName}<br/> <span class="white1">{blogName}</span></h1>
                                    <p>{des}</p>
                                    <a href="#">{t('red.1')}</a>
                                    </div>
                                </div>
                                <div class="col-xl-4 col-lg-4 col-md-4 col-12-3">
                                    <div class="text-img">
                                    <figure><img src={img2} alt="#"/></figure>
                                    </div>
                                </div>
                            </div>
                        </div>
                        </section>
                    </div>
                </header>
                {/* <!-- end banner -->
                <!-- blog_main --> */}
                <div class="blog_main">
                    <div class="container">
                        <div class="row">
                        <div class="col-md-12">
                            <div class="titlepage">
                                <h2>{t('bl.1')}</h2>
                                <span>{t('bl1.1')}</span>
                            </div>
                        </div>
                        </div>
                        {/* <!-- fist section --> */}
                        <div class="row">
                        <div class="col-md-12">
                            <div class="our_two_box">
                                <div class="row d_flex">
                                
                                    <div class="col-xl-6 col-lg-6 col-md-12 col-sm-12">
                                    <div class="our_img">
                                        <figure><img src={img3} alt="#"/></figure>
                                    </div>
                                    </div>
                                    <div class="col-xl-6 col-lg-6 col-md-12 col-sm-12">
                                    <div class="our_text_box">
                                        <h3 class="awesome pa_wi">{t('bl1.1')}</h3>
                                        <p>{t('bl2.1')}</p>
                                        <div class="post_box padding_bottom1">
                                            <h4 class="flot_left1">{t('bl3.1')}</h4>
                                            <ul class="like">
                                                <li><a href="#"><img src={img4} alt="#"/>{t('lk.1')}</a></li>
                                                <li><a href="#"><img src={img5} alt="#"/>{t('cmn.1')}</a></li>
                                            </ul>
                                        </div>
                                    </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        </div>
                {/* <!-- end fist section -->
                <!-- secend section --> */}
                        <div class="row">
                        <div class="col-md-12">
                            <div class="our_two_box">
                                <div class="row">
                                    <div class="col-md-12">
                                    <div class="our_img">
                                        <figure><img class="he_img" src={img6} alt="#"/></figure>
                                    
                                    
                                    <div class="our_text_box position_box">
                                        <h3 class="awesome withi_color">{t('ms.1')} </h3>
                                        <p class="hiuouh">{t('bl2.1')}</p>
                                        <div class="post_box">
                                            <h4 class="flot_left1 withi_color">{t('bl3.1')}</h4>
                                            <ul class="like withi_color">
                                                <li><a href="#"><img src={img7} alt="#"/>{t('lk.1')}</a></li>
                                                <li><a href="#"><img src={img8} alt="#"/>{t('cmn.1')}</a></li>
                                            </ul>
                                        </div>
                                    </div>
                                    </div>
                                    
                                    </div>
                                </div>
                            </div>
                        </div>
                        </div>
                        {/* <!-- end secend section --> */}

                    </div>
                </div>
                {/* <!-- end blog_main -->
                
            

                <!--  footer --> */}
                <footer>
                    <div class="footer">
                        <div class="container">
                        <div class="row">
                            <div class="col-md-12 ">
                            </div>
                            <div class="col-md-12">
                                <ul class="social_icon">
                                    <li><a href="#"><i class="fa fa-facebook" aria-hidden="true"></i></a></li>
                                    <li><a href="#"><i class="fa fa-twitter" aria-hidden="true"></i></a></li>
                                    <li><a href="#"><i class="fa fa-linkedin" aria-hidden="true"></i></a></li>
                                </ul>
                            </div>
                        </div>
                        </div>
                        <Contact/>
                    </div>
                </footer>
                {/* //   <!-- end footer --> */}
                
                </body>
        </div>
    );
}

export default Home;