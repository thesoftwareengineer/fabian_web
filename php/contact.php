<?php
    //require_once 'swiftmailer/swiftmailer/lib/swift_required.php';
    require '../vendor/autoload.php';

    $name = $_POST['name'];
    $email = $_POST['email'];
    $number = $_POST['number'];
    $body = $_POST['message'];
    $email_message .= "Name: ".$name."\n";
    $email_message .= "Email: ".$email."\n";
    $email_message .= "Telephone: ".$number."\n";
    $email_message .= "Message: ".$body."\n";
    $email_to = 'egonzalezjr555@gmail.com';
    $email_subject = "Leon Website Request";
    $transport = \Swift_SmtpTransport::newInstance('xo7.x10hosting.com', 465,'ssl')->setUsername('sender@dataoverflow.elementfx.com')->setPassword('*******');

    $mailer = \Swift_Mailer::newInstance($transport);
    $message = \Swift_Message::newInstance('Our Code World Newsletter')
       ->setFrom(array('sender@dataoverflow.elementfx.com' => 'Leon contact'))
       ->setTo(array($email_to => "mail@mail.com"))
       ->setBody($email_message);
    $result = $mailer->send($message);
    if ($result) {
        echo '<script type="text/javascript"> alert ("Thank you '.$name.' we have submitted your message and we will get back to you as soon as possible."); window.history.back();</script>';
    }
    else {
        echo '<script type="text/javascript"> alert ("Sorry '.$name.' please try again."); window.history.location ="../index.html"; </script>';
    }
?>
