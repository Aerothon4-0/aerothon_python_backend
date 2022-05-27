import React from 'react';
import { useTranslation } from 'react-i18next';
import '../Contact.css'

function Contact() {
    
    const { t, i18n } = useTranslation();
    return (
        <div className="container contact-form" id='contact_part'>
            <div className="contact-image">
                <img src="https://image.ibb.co/kUagtU/rocket_contact.png" alt="rocket_contact"/>
            </div>
            <form method="post">
                <h3>{t('msg1.1')}</h3>
               <div className="row">
                    <div className="col-md-6">
                        <div className="form-group">
                            <input type="text" name="txtName" className="form-control" placeholder={t('msg2.1')} value="" />
                        </div>
                        <div className="form-group">
                            <input type="text" name="txtEmail" className="form-control" placeholder={t('msg3.1')} value="" />
                        </div>
                        <div className="form-group">
                            <input type="text" name="txtPhone" className="form-control" placeholder={t('msg4.1')} value="" />
                        </div>
                        <div className="form-group">
                            <input type="submit" name="btnSubmit" className="btnContact" value={t('msg6.1')} />
                        </div>
                    </div>
                    <div className="col-md-6">
                        <div className="form-group">
                            <textarea name="txtMsg" className="form-control" placeholder={t('msg5.1')} style={{width: "100%",height: "150px"}}></textarea>
                        </div>
                    </div>
                </div>
            </form>
</div>
    );
}

export default Contact;