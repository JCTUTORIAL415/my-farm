<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = $_POST["name"];
    $email = $_POST["email"];
    $message = $_POST["message"];
    
    $to = "gaiyas.iot.agriculture.tw@gmail.com";
    $subject = "新消息来自联系我们页面";
    $body = "姓名: $name\n";
    $body .= "邮箱: $email\n";
    $body .= "消息: $message\n";
    
    if (mail($to, $subject, $body)) {
        echo "消息发送成功！";
    } else {
        echo "发送消息时出错，请重试。";
    }
}
?>
