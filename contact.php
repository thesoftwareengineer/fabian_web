<?php
    require_once './vendor/swiftmailer/swiftmailer/lib/swift_required.php';
    $name = $_POST['name'];
    $email = $_POST['email'];
    $number = $_POST['number'];
    $body = $_POST['message'];
    $email_message .= "Name: ".$name."\n";
    $email_message .= "Email: ".$email."\n";
    $email_message .= "Telephone: ".$number."\n";
    $email_message .= "Message; ".$body."\n";
    $email_to = 'egonzalezjr555@mgmail.com';
    $email_subject = "Fabian Website";

    $transport = \Swift_SmtpTransport::newInstance()
            ->setUsername('data.overflow@hotmail.com')->setPassword('******')
            ->setHost('smtp-mail.outlook.com')
            ->setPort(587)->setEncryption('tls');

    $mailer = \Swift_Mailer::newInstance($transport);

    $message = \Swift_Message::newInstance()
       ->setSubject($email_subject)
       ->setFrom(array('data.overflow@hotmail.com' => 'Email'))
       ->setTo(array($email_to))
       ->addPart($email_message)
        ;

    $result = $mailer->send($message);
    if ($result) {
        echo "Message Sent Successfully!";
    }
    else {
        "Please fix the fields";
    }
?>
