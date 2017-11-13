<!-- Database Access & Query -->
<?php
    // access mysql database access parameters
    // config file MUST be created outside the root directory of the website
    $configs = include('../config/config.php');
    $servername = $configs['host'];
    $username = $configs['username'];
    $password = $configs['password'];
    $database = $configs['database'];

    // Create connection
    $conn = mysqli_connect($servername, $username, $password);
    mysqli_select_db($conn, $database);        

    // SQL query for total species count
    $speciescount = "select count(*) from species_info";
    $runresult1 = mysqli_query($conn, $speciescount); // retrieve results from DB
    $speciescount = mysqli_fetch_array($runresult1); // put results in arrary
    $speciescount = $speciescount[0];

    //sql query to get top 9 species by date
    $query = "select concat(genus, ' ', species) as speciesnm, url_imgthumb, url
                from species_info 
                order by posted_date desc 
                limit 9";
    $run_result = mysqli_query($conn, $query);  
    
    //get top 9 species into multidimenstional array
    $i=0;
    while($values = mysqli_fetch_array($run_result)){
        $speciesnm[$i] = $values['speciesnm'];
        $imgthumb[$i] = $values['url_imgthumb'];
        $url[$i] = $values['url'];
        $i++;
    }
?>


<!-- Count Directory Files for # Images -->
<?php echo (count(scandir('./images')) - 2)?>
<!-- Echo Species Count -->
<?php echo"$speciescount"?>
<!-- Echo Family Count -->
<?php echo"$familycount"?>


<div class="col-xs-6 col-sm-4 col-md-3 thumb_height_home">
    <div class="thumbnail">
        <!-- Echo Link of Species Page -->
        <a href="<?php echo"$url[0]"?>">
            <!-- Echo Directory Path of Image -->
            <img class="img-responsive img-hover img-rounded" src="<?php echo "$imgthumb[0]"?>" alt="">
        </a>
        <div class = "caption">
            <!-- Echo Species Name -->
            <h_caption><?php echo"$speciesnm[0]";?></h_caption>
        </div>
    </div>
</div>

<!-- ECHO -->
<?php
  $test = 1;
  echo $test;
  echo ($test);
  echo "$test";
?>

<!-- ESCAPE CHARACTERS ---------------------------------------------->
<!-- for normal single escape, use \ -->
<?php <a href="../$url_family[$i]">$family[$i]</a> ?>

<!-- to escape all quotes in echo, use "<<<" with a variable name. 
      note that closing variable can only have ";" with no spaces -->
<?php echo <<< heredoc
    <p>
      <strong>Family</strong>: <a href="../$url_family[$i]">$family[$i]</a>
    </p>
heredoc;
?>



<?php
  // PRINTING
  // --------------------------------------------
  $test = "testing"
  print_r($test); // print actual value / array
  var_dump($test); // like print_r but with type & # char. Also prints False
  

  // CONCAT
  // --------------------------------------------
  // concat using .
  $x = "this" . " " . "is great";
  echo "$x";
  
  // we can use .= for string concat too
  $test = "this is";
  $test .= " a test";
  echo ($test);
  
  
  // CONDITION
  // --------------------------------------------
  // ternary ?:
  $www = 123;
  $msg = ($www > 100) ? "Large" : "Small"
  echo "$msg" # Large
  
  // if
  if (123 > 100 == 1) print "True"; // equality will convert True/False to 1/0 or TRUE/FALSE depending on condition type
  if (123 > 100 === TRUE) print "True"; // identity suppresses type conversion, True/False will remain string
  
  // if else
  if (123 > 100 === TRUE)
      {print "True";}
  elseif (5 > 10) // a boolean
      {print "maybe";}
  else 
      {print "False";}
  
  // string position
  $test = "test"; 
  echo strpos($test, "es"); // careful using strpos as a condition, use === to evaluate as False is 0 & position 1 is also 0
  
  // LOOPS
  // --------------------------------------------
  // while loop
  $fuel = 10;
  while ($fuel < 1) {
    print "vroom vroom\n";
    $fuel = $fuel - 1
  }
  
  // for loops (linear array)
  for ($count=0; $count<count($array); $count++) { //start, end if, after each loop
    echo "$i, $stuff[$i]\n";
  }
  
  // for each loop (array looping)
  foreach($stuff as $key => $value){
    echo "$key: $value\n";
  }
  
  
  // CAST
  // --------------------------------------------
  echo (int)9.9 + 1
  echo "sam" . 25 // . will force convert 25 into string
  echo "25" + 25 // + will force convert "25" into number
?>

<?php
  // ARRAY 
  // --------------------------------------------
  $stuff = array("hi", "there");
  echo $stuff[0]; // hi
  
  $stuff = array("name" => "Jake",
                 "country" => "Asia");
  echo $stuff["name"];
  
  // print exact array with preserved indent
  echo "<pre>";
  print_r($stuff);
  echo "</pre>";
  
  // add stuff to array, must be new field
  $stuff["name2"] = "Emila";
  
  // NESTED ARRAYS
  $products = array(
              "paper" => array(
                  "copier" => "Multipurpose",
                  "inkjet" => "Inkjet Printer"
                  )
              );
  echo $products["paper"]["copier"]; // Multipurpose
  
  // check for key availability 
  echo $stuff["name"] ?? 'nobody'; // if yes print name, else print "nobody" (from PHP 7)
  echo isset($stuff["name"]) ? $stuff["name"]: "nobody"; 
  
  // SORTING, function will change the array, print again to see the change
  sort($array) // sorts array values (loses keys)
  ksort($array) // sorts array by keys
  asort($array) // sorts array by values (keeping keys)
  shuffle($array) // sorts randomly
  print_r($array)
  
  // SORT
  // Array
  // (
  //     [0] => Asia
  //     [1] => Emila
  //     [2] => Jake
  // )
  
  
  // STRING TO ARRAY
  $sentence = "this is a sentence";
  $explode = explode(' ', $sentence);
  print_r($explode);
  
  // Array
  // (
  //     [0] => this
  //     [1] => is
  //     [2] => a
  //     [3] => sentence
  // )
?>
