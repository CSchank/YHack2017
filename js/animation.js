
var info = {
    firstName: null,
    lastname: null,
    email: null,
    city: null,
    longitude: null,
    latitude: null,
    address: null,
    state: null,
    maritalstatus: null,
    employmentstatus: null,
    annualincome: null,
    dependents: null,
    age: null,
    sex: null,
    height: null,
    weight: null,
    tobacco: null,
    medical: [],
    total: 500000,
}
var url = "http://159.203.2.233/quote"
var mednum = 0;
var response = {
    "bronze": 500,
    "silver": 600,
    "gold": 700,
    "platinum": 800,
    "purchase": 1,
};


function getNextForm(param) {
        switch (param) {
            case (1):
                var elem = document.getElementById("one");
                info.firstName = document.getElementById("fname").value;
                if (!info.firstName) {
                    alert("Invalid first name");
                    return;
                }
                info.lastName = document.getElementById("lname").value;
                if (!info.lastName) {
                    alert("Invalid last name");
                    return;
                }
                info.email = document.getElementById("email").value;
                if (!info.email) {
                    alert("Invalid email");
                    return;
                }
                info.address = document.getElementById("address").value;
                if (!info.address) {
                    alert("Invalid address");
                    return;
                }
                info.city = document.getElementById("city").value; //selecting
                if (!info.city) {
                    alert("Invalid city");
                    return;
                }
                $.getJSON("http://maps.googleapis.com/maps/api/geocode/json?address="+info.city, function(val) {
                    if(val.results.length) {
                        console.log("query success");
                      var location = val.results[0].geometry.location;
                      info.latitude = location.lat;
                      info.longitude = location.lng;
                    }
                    else alert("Invalid city");
                    return;
                })
                info.state = document.getElementById("state").value; //selecting
                if (!info.state) {
                    alert("Invalid state");
                    return;
                }
                animatenone(elem);
                changeTransparency("two");
                break;
            case (2):
                var elem = document.getElementById("two");
                info.maritalstatus = document.getElementById("mar").checked? 1 : 0;
                info.employmentstatus = document.getElementById("emp").checked? 1 : 0;
                info.annualincome = document.getElementById("ann").value; //number between range
                if (!info.annualincome || info.annualincome < 0 || info.annualincome > 1000000) {
                    alert("Please enter income in range 0 to 1000000");
                    return;
                }
                info.dependents = document.getElementById("dep").value; //1, 2, 3, 4
                if (info.dependents < 1 || info.dependents > 4) {
                    alert("Please enter dependents in range 1 to 4");
                    return;
                }
                animatenone(elem);
                changeTransparency("three");
                break;
            case (3):
                var elem = document.getElementById("three");
                info.age = document.getElementById("age").value; //min 18, max 99
                if (info.age < 18 || info.age > 99) {
                    alert("Please enter age in range 18 and 99");
                    return;
                }
                info.sex = document.getElementById("sex").value; //'M' or 'F' m is 0, F is 1
                if (!(info.sex == "F" || info.sex == "M")) {
                    alert("Please enter M or F for sex");
                    return;
                }
                info.height = document.getElementById("height").value; //50max is 80
                if (info.height < 50 || info.height > 80) {
                    alert("Please enter height in range 50 and 80");
                    return;
                }
                info.weight = document.getElementById("weight").value; //100max is 300
                if (info.weight < 100 || info.weight > 300) {
                    alert("Please enter weight in range 100 and 300");
                    return;
                }
                info.tobacco = document.getElementById("tob").checked? 1 : 0;
                animatenone(elem);
                changeTransparency("four");
                break;
            case (4):
                var elem = document.getElementById("four");
                for (var i = 0; i <= mednum; i++) {
                    var med = document.getElementById("med"+i).value.split(" ")[0];
                    if (!med) continue;
                    var risk = document.getElementById("risk"+i).value;
                    if (risk != "Low" && risk != "Medium" && risk != "High" && med) {
                        alert("Risk must be 'Low', 'Medium', or 'High'.");
                        return;
                    }
                    info.medical.push({"ICD_CODE": med, "Risk_factor": risk});
                }
                animatenone(elem);
                changeTransparency("five");
                break;
            case (5):
                var elem = document.getElementById("five");
                info.total = info.total + document.getElementById("additional").value * 10000;
                animatenone(elem);
                console.log(info);
                submit();
                break;
    }
}

function submit() {
    var xhr = new XMLHttpRequest();
    xhr.open("POST", url, true);
    xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xhr.send(JSON.stringify(info));
    xhr.onload = function() {
        console.log(xhr.status);
        console.log(xhr.responseText);
        response = JSON.parse(xhr.responseText);
        loadPlans();
        $("#loading").addClass("undisplay");
    }
    console.log(xhr.status);
    console.log(xhr.responseText);
    produceLoading();

}

function produceLoading() {
    $("#loading").removeClass("undisplay");
}

function loadPlans() {
    $("#blocker").addClass("undisplay");
    var plan;
    var price;
    var key;
    switch(response.purchase) {
        case 0:
            plan = "Bronze";
            key = "bronze";
            price = response.bronze;
            break;
        case 1:
            plan = "Silver";
            key = "silver";
            price = response.silver;
            break;
        case 2:
            plan = "Gold";
            key = "gold";
            price = response.gold;
            break;
        case 3:
            plan = "Platinum";
            key = "platinum";
            price = response.platinum;
            break;
        default:
            alert("error");
    }
    // $("#preferred").html(function() {
    //     return plan + "<br> $" + price;
    // });
    // $("#preferred").removeClass("undisplay");
    // $("#preferred").addClass(key);
    $("#title").children().text("Your preferred plan: "+plan);
    for (var i = 0; i < 4; i++) {
            var  block = "#resultblock"+i;
            console.log(block);

            switch (i) {
                case 0:
                    $(block).html(function() {
                        return "Bronze <br> $" + response.bronze;
                    });
                    break;
                case 1:
                    $(block).html(function() {
                        return "Silver <br> $" + response.silver;
                    });
                    break;
                case 2:
                    $(block).html(function() {
                        return "Gold <br> $" + response.gold;
                    });
                    break;
                case 3:
                    $(block).html(function() {
                        return "Platinum <br> $" + response.platinum;

                    });
                    break;
            }
            $(block).removeClass("undisplay");
            if (i == response.purchase) {
                console.log("found match")
                $(block).css({
                         "border-width": "5px",
                        "border-color":"#fff",
                        "border-style": "solid"})
            };
    }
    $("#results").removeClass("undisplay");
}

function changeTransparency(elem, transparency) {
    var e = document.getElementById(elem);
    e.classList.remove("semitransparent");
}


function changeTransparencyWithBorder(elem, transparency) {
    var e = document.getElementsByClassName(elem);
    e.style.color = "rgba(255,255,255,"+transparency+")";
    e.style.borderBottomColor = "rgba(255,255,255,"+transparency+")";
}

function addForm() {
    if (mednum >= 5) {
        alert("maximum of 5 rows");
        return;
    }
    mednum++;
    // var e = document.getElementById("medical-form");
    $("#med0").clone().prop({ id: "med"+ mednum }).appendTo("#med-container");
    $("#risk0").clone().prop({ id: "risk"+ mednum }).appendTo("#med-container");
    var demo = new autoComplete({
            selector: '#med'+mednum,
            minChars: 1,
            source: function(term, suggest){
                term = term.toLowerCase();
                var choices = ["A15-A19 Tuberculosis","B20-B20 Human immunodeficiency virus [HIV] disease","D50-D53 Nutritional anemias","E08-E13 Diabetes mellitus","E65-E68 Overweight, obesity and other hyperalimentation","E73 Lactose intolerance","E84 Cystic fibrosis","F20-F29 Schizophrenia, schizotypal, delusional, and other non-mood psychotic disorders","F70-F79 Intellectual disabilities","G10 Huntington's disease","G11 Hereditary ataxia","G20 Parkinson's disease","G30 Alzheimer's disease","G35 Multiple sclerosis","G40 Epilepsy and recurrent seizures","G43 Migraine","G47 Sleep disorders","G80 Cerebral palsy","G91 Hydrocephalus","G92 Toxic encephalopathy","H40-H42 Glaucoma","H80 Otosclerosis","I10-I16 Hypertensive diseases","I20-I25 Ischemic heart diseases","I26 Pulmonary embolism","I30 Acute pericarditis","I40 Acute myocarditis","I46 Cardiac arrest","I50 Heart failure","I63 Cerebral infarction","I95 Hypotension","J09-J18 Influenza and pneumonia","J81 Pulmonary edema","K35 Acute appendicitis","K40-K46 Hernia","K50 Crohn's disease [regional enteritis]","K51 Ulcerative colitis","K65 Peritonitis","K70 Alcoholic liver disease","K74 Fibrosis and cirrhosis of liver","K85 Acute pancreatitis","L20 Atopic dermatitis","L21 Seborrheic dermatitis","L22 Diaper dermatitis","L23 Allergic contact dermatitis","L24 Irritant contact dermatitis","L40 Psoriasis","L41 Parapsoriasis","L60 Nail disorders","L70 Acne","L71 Rosacea","L80 Vitiligo","L89 Pressure ulcer","M08 Juvenile arthritis","M10 Gout","M1A Chronic gout","M15-M19 Osteoarthritis","N17 Acute kidney failure","N18 Chronic kidney disease (CKD)","N46 Male infertility","N52 Male erectile dysfunction","N91 Absent, scanty and rare menstruation","N92 Excessive, frequent and irregular menstruation","N96 Recurrent pregnancy loss","N97 Female infertility","Q02 Microcephaly","Q05 Spina bifida","Q35-Q37 Cleft lip and/or cleft palate","Q61 Cystic kidney disease","Q90 Down syndrome","Q91 Trisomy 18 and Trisomy 13","Q96 Turner's syndrome","R17 Unspecified jaundice","S00-S09 Injuries to the head","S10-S19 Injuries to the neck","T33-T34 Frostbite","Z66-Z66 Do not resuscitate status","Z68-Z68 Body mass index (BMI)"];
                var suggestions = [];
                for (i=0;i<choices.length;i++)
                    if (~choices[i].toLowerCase().indexOf(term)) suggestions.push(choices[i]);
                suggest(suggestions);
            }
        });
}

function removeForm() {
    if (mednum < 0) {
        return;
    }

    // var e = document.getElementById("medical-form");
    $("#med"+mednum).remove();
    $("#risk"+mednum).remove();
    mednum--;
}

// Update the current slider value (each time you drag the slider handle)
function updateSliderValue(value) {
    var output = document.getElementById("slideroutput");
    output.innerHTML = value * 10000;
}

function animatenone(element) {
    transition.begin(element, ["opacity", "1", "0", "500ms", "linear"], {onTransitionEnd: function() {element.style.display = 'none';}});
}

