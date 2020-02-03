$(function(){
  
    $("#menu-toggle").click(function(e) {       
        $("#wrapper").toggleClass("active");
    });


  
   $("#form-total").steps({
        headerTag: "h2",
        bodyTag: "section",
        transitionEffect: "fade",        
        autoFocus: true,
        transitionEffectSpeed: 500,
        titleTemplate : '<div class="title">#title#</div>',
     
        labels: {
            previous : 'Previous',
            next : 'Next',
            finish : '',
            current : ''
        }, 
        

        onStepChanged: function (event, currentIndex, newIndex) {
       
            if (currentIndex < newIndex) {
                $('.steps li.current').next().removeClass('done');                                  
              }
              var $input = $('#submittrade');
              if (currentIndex === 3) { //if last step             
                //remove default #finish button
                var $input = $('#submittrade');
                $input.appendTo($('a[href="#finish"]'));
               }
               else {
                //$('ul[aria-label=Pagination] button').remove();
                $('ul[aria-label=Pagination] button').appendTo($('a[href="#finish"]'));            
               }
           
        },

        onStepChanging: function (event, currentIndex, newIndex) {         
            
           //Trade values- Form 1
            
            var dispatch=$('#dispatch').val();
            var trad_price=$('#trad_price').val(); 
            var dispatch=$('#dispatch').val();
            var tconfirmno = $('#tconfirmno').val();
            var tconfirmdate = $('#tconfirmdate').val();
            var tbuyername = $('#tbuyername').val();
            var tgstin_b = $('#tgstin_b').val();
            var tdoor_add = $('#tdoor_add').val();
            var tstate = $('#tstate').val();
            var tpincode = $('#tpincode').val();
            var sellername = $('#sellername').val();
            var tgstin_s = $('#tgstin_s').val();
            var tradername = $('#tradername').val();
            var tradertype = $('#tradertype').val();
            var tbrokername = $('#tbrokername').val();
            var tbroker_cno = $('#tbroker_cno').val();
            var tbrokeremail = $('#tbrokeremail').val();
            var tcommiss = $('#tcommiss').val();


            var tstation = $('#tstation').val();
            var tstate_qual = $('#tstate_qual').val();
            var tvariety = $('#tvariety').val();
            var tstaple = $('#tstaple').val();
            var tmicfrom = $('#tmicfrom').val();
            var tmicto = $('#tmicto').val();
            var tgtex = $('#tgtex').val();
            var tgrade = $('#tgrade').val();
            var ttrash = $('#ttrash').val();
            var tmositure = $('#tmositure').val();
            var thsn = $('#thsn').val();
            var tbales = $('#tbales').val();
            var ttruck = $('#ttruck').val();
            var tprice = $('#tprice').val();


            var termdel = $('#termdel').val();
            var tgst = $('#tgst').val();
            var tdispatch = $('#tdispatch').val();
         
            var termpay = $('#termpay').val();
            var tfirstpay = $('#tfirstpay').val();           
            var tfirstpayday = $('#tfirstpayday').val();
            var tsecondpayper = $('#tsecondpayper').val();
            var tsecondpayday = $('#tsecondpayday').val();
            var tinterestlate = $('#tinterestlate').val();
            var tweighment = $('#tweighment').val();
            var tpassing = $('#tpassing').val();
            var transit_insur = $('#transit_insur').val();
            var tmillgateno = $('#tmillgateno').val();
            var tnotes = $('#tnotes').val();         
   
         

           //trade form1
   
            $('#tconfirmno-val').text(tconfirmno);
            $('#tconfirmdate-val').text(tconfirmdate);
            $('#tbuyername-val').text(tbuyername);
            $('#tgstin_b-val').text(tgstin_b);
            $('#tdoor_add-val').text(tdoor_add);
            $('#tstate-val').text(tstate);
            $('#tpincode-val').text(tpincode);            
            $('#sellername-val').text(sellername);
            $('#tgstin_s-val').text(tgstin_s);
            $('#tradername-val').text(tradername);
            $('#tradertype-val').text(tradertype);
            $('#tbrokername-val').text(tbrokername);
            $('#tbroker_cno-val').text(tbroker_cno);
            $('#tbrokername-val').text(tbrokername);
            $('#tbrokeremail-val').text(tbrokeremail);
            $('#tcommiss-val').text(tcommiss);

            $('#tstation-val').text(tstation);
            $('#tstate_qual-val').text(tstate_qual);
            $('#tvariety-val').text(tvariety);
            $('#tstaple-val').text(tstaple);
            $('#tmicfrom-val').text(tmicfrom);
            $('#tmicto-val').text(tmicto);
            $('#tgtex-val').text(tgtex);
            $('#tgrade-val').text(tgrade);
            $('#ttrash-val').text(ttrash);
            $('#tmositure-val').text(tmositure);
            $('#thsn-val').text(thsn);
            $('#ttruck-val').text(ttruck);
            $('#tprice-val').text(tprice);
            $('#termdel-val').text(termdel);
            $('#tgst-val').text(tgst);
            $('#tdispatch-val').text(tdispatch);
            $('#ttruck-val').text(ttruck);          
            $('#termpay-val').text(termpay);
            $('#tfirstpay-val').text(tfirstpay);
            $('#tsecondpayper-val').text(tsecondpayper);
            $('#tfirstpayday-val').text(tfirstpayday);
            $('#tsecondpayday-val').text(tsecondpayday);
            $('#tinterestlate-val').text(tinterestlate);
            $('#tweighment-val').text(tweighment);        
            $('#tpassing-val').text(tpassing);
            $('#transit_insur-val').text(transit_insur);        
            $('#tmillgateno-val').text(tmillgateno);
            $('#tnotes-val').text(tnotes);

              //form 2          
              $('#tconfirmno-val1').text(tconfirmno);
              $('#tconfirmdate-val1').text(tconfirmdate);
              $('#tbuyername-val1').text(tbuyername);
              $('#tgstin_b-val1').text(tgstin_b);
              $('#tdoor_add-val1').text(tdoor_add);
              $('#tstate-val1').text(tstate);
              $('#tpincode-val1').text(tpincode);            
              $('#sellername-val1').text(sellername);
              $('#tgstin_s-val1').text(tgstin_s);
              $('#tradername-val1').text(tradername);
              $('#tradertype-val1').text(tradertype);
              $('#tbrokername-val1').text(tbrokername);
              $('#tbroker_cno-val1').text(tbroker_cno);
              $('#tbrokername-val1').text(tbrokername);
              $('#tbrokeremail-val1').text(tbrokeremail);
              $('#tcommiss-val1').text(tcommiss);
  
              $('#tstation-val1').text(tstation);
              $('#tstate_qual-val1').text(tstate_qual);
              $('#tvariety-val1').text(tvariety);
              $('#tstaple-val1').text(tstaple);
              $('#tmicfrom-val1').text(tmicfrom);
              $('#tmicto-val1').text(tmicto);
              $('#tgtex-val1').text(tgtex);
              $('#tgrade-val1').text(tgrade);
              $('#ttrash-val1').text(ttrash);
              $('#tmositure-val1').text(tmositure);
              $('#thsn-val1').text(thsn);
              $('#ttruck-val1').text(ttruck);
              $('#tprice-val1').text(tprice);
              $('#termdel-val1').text(termdel);
              $('#tgst-val1').text(tgst);
              $('#tdispatch-val1').text(tdispatch);
              $('#ttruck-val1').text(ttruck);          
              $('#termpay-val1').text(termpay);
              $('#tfirstpay-val1').text(tfirstpay);
              $('#tsecondpayper-val1').text(tsecondpayper);
              $('#tfirstpayday-val1').text(tfirstpayday);
              $('#tsecondpayday-val1').text(tsecondpayday);
              $('#tinterestlate-val1').text(tinterestlate);
              $('#tweighment-val1').text(tweighment);        
              $('#tpassing-val1').text(tpassing);
              $('#transit_insur-val1').text(transit_insur);        
              $('#tmillgateno-val1').text(tmillgateno);
              $('#tnotes-val1').text(tnotes);
  
              //form 3          
              $('#tconfirmno-val2').text(tconfirmno);
            $('#tconfirmdate-val2').text(tconfirmdate);
            $('#tbuyername-val2').text(tbuyername);
            $('#tgstin_b-val2').text(tgstin_b);
            $('#tdoor_add-val2').text(tdoor_add);
            $('#tstate-val2').text(tstate);
            $('#tpincode-val2').text(tpincode);            
            $('#sellername-val2').text(sellername);
            $('#tgstin_s-val2').text(tgstin_s);
            $('#tradername-val2').text(tradername);
            $('#tradertype-val2').text(tradertype);
            $('#tbrokername-val2').text(tbrokername);
            $('#tbroker_cno-val2').text(tbroker_cno);
            $('#tbrokername-val2').text(tbrokername);
            $('#tbrokeremail-val2').text(tbrokeremail);
            $('#tcommiss-val2').text(tcommiss);

            $('#tstation-val2').text(tstation);
            $('#tstate_qual-val2').text(tstate_qual);
            $('#tvariety-val2').text(tvariety);
            $('#tstaple-val2').text(tstaple);
            $('#tmicfrom-val2').text(tmicfrom);
            $('#tmicto-val2').text(tmicto);
            $('#tgtex-val2').text(tgtex);
            $('#tgrade-val2').text(tgrade);
            $('#ttrash-val2').text(ttrash);
            $('#tmositure-val2').text(tmositure);
            $('#thsn-val2').text(thsn);
            $('#ttruck-val2').text(ttruck);
            $('#tprice-val2').text(tprice);
            $('#termdel-val2').text(termdel);
            $('#tgst-val2').text(tgst);
            $('#tdispatch-val2').text(tdispatch);
            $('#ttruck-val2').text(ttruck);          
            $('#termpay-val2').text(termpay);
            $('#tfirstpay-val2').text(tfirstpay);
            $('#tsecondpayper-val2').text(tsecondpayper);
            $('#tfirstpayday-val2').text(tfirstpayday);
            $('#tsecondpayday-val2').text(tsecondpayday);
            $('#tinterestlate-val2').text(tinterestlate);
            $('#tweighment-val2').text(tweighment);        
            $('#tpassing-val2').text(tpassing);
            $('#transit_insur-val2').text(transit_insur);        
            $('#tmillgateno-val2').text(tmillgateno);
            $('#tnotes-val2').text(tnotes);


            $("#form-register").validate().settings.ignore = ":disabled,:hidden";
            return $("#form-register").valid();
           
        }
    }); 
});

//Payment options
$(document).ready(function(){

    $("#tfirstpa").prop("disabled", true);
    $("#tfirstpayday").prop("disabled", true);
    $("#tsecondpayper").prop("disabled", true);
    $("#tsecondpayday").prop("disabled", true);
    
    
    $("#termpay").change(function() {
        if ($(this).val() == "partial") {  

        $("#tfirstpa").prop("disabled", false);
        $("#tfirstpayday").prop("disabled", false);
        $('#tsecondpayper').prop('disabled',false);
        $("#tsecondpayday").prop("disabled", false);
        $("#tfirstpa").css("background-color", "white");
         $("#tfirstpayday").css("background-color", "white");
        $("#tsecondpayper").css("background-color", "white");
        $("#tsecondpayday").css("background-color", "white");
        }
        else
       {
        $("#tfirstpayday").prop("disabled", true);
        $("#tfirstpa").prop("disabled", true);
        $('#tsecondpayper').prop('disabled',true);
        $('#tsecondpayday').prop('disabled',true);
       }
    });

 
 
});
// $('.wizard').find('a[href="#finish"]').remove(); 
                //append a submit type button
               // $('.wizard .actions ul li:last-child').append('<button type="submit" class="btnsubmit" id="submittrade" class="btn-large">Submit</button>');
       
