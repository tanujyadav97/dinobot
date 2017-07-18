<!DOCTYPE>
<html lang-en>
    <head>
        <link rel="stylesheet" type="text/css" href="chathere-css.css">
    </head>

    <body>
        <h1>Chat with the bot here</h1>

        <div id="chatshow">
            <ul id="chatlist">
                <?php
                 $myfile=fopen("chat.txt","r") or die("unable to open file");
                 while(!feof($myfile))
                {
                    $line=fgets($myfile);
                    $str=explode('###',$line);
                    if(!isset($str[1]))
                    $str[1]=null;
                    $part=explode('<>',$str[1]);
                    $joined=join('<br/>',$part);
                    if($str[0]=='1')
                    { ?>
                    <li class="type1">
                    <?php echo $joined; ?>    
                    </li>   
                    <?php } else {?>
                    <li class="type2">
                    <?php echo $joined; ?>    
                    </li>   
                    <?php }
                 }
                ?>
            </ul>
        </div>

        <textarea id="message"></textarea>

        <button id="post">Post</button>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script>

<script src="chat.js"></script>

    </body>
</html>