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
            current : '',
            
        }, 
        
        
        onStepChanged: function (event, currentIndex, newIndex) {
            if (currentIndex < newIndex) {
                $('.steps li.current').next().removeClass('done');                                  
              }
              var $input = $('#submitvendor');
              if (currentIndex === 2) { //if last step             
                
                $('.actions > ul > li:last-child').attr('style', 'display:none');              
               $('ul[aria-label=Pagination] button').remove();
                var $input = $('#submitvendor');
                $input.appendTo($('ul[aria-label=Pagination]'));                
                $input.attr('style', 'display:block');              
               }
               else {               
                //$('ul[aria-label=Pagination] input[value="Submit"]').remove();      
                //$('ul[aria-label=Pagination] input[value="Submit"]').appendTo($('a[href="#finish"]'));        
               }
              
        },

              
       onStepChanging: function (event, currentIndex, newIndex) { 
   
        if (currentIndex === 2) { 
            $('ul[aria-label=Pagination] input[value="Submit"]').appendTo($('a[href="#finish"]'));   
        }

            var vendortype = $('#vendortype').val();
            var company_email = $('#company_email').val();
            var company_name = $('#company_name').val();
            var adddoor = $('#adddoor').val();
            var locality = $('#locality').val();
            var state = $('#state').val();
            var pincode = $('#pincode').val();
            var proprietorDirectorName = $('#proprietorDirectorName').val();
            var proprietorDirectorContact = $('#proprietorDirectorContact').val();
            var local_contact_name = $('#local_contact_name').val();
            var local_contact_no = $('#local_contact_no').val();


            var gstin = $('#gstin').val();
            var uin = $('#uin').val();
            var pan = $('#pan').val();

            var accountno = $('#accountno').val();
            var accountname = $('#accountname').val();
            var ifsc = $('#ifsc').val();
            var bankname = $('#bankname').val();
            var branch = $('#branch').val();
            var accounttype = $('#accounttype').val();
            var insurno = $('#insurno').val();
            var expirdate1 = $('#expirdate1').val();
            var expirdate2 = $('#expirdate2').val();
            var insurname = $('#insurname').val();    

         
        
             //vendor

             $('#vendortype-val').text(vendortype);
             $('#company_email-val').text(company_email);
             $('#company_name-val').text(company_name);
             $('#adddoor-val').text(adddoor);
             $('#locality-val').text(locality);
             $('#state-val').text(state);
             $('#pincode-val').text(pincode);
             $('#proprietorDirectorName-val').text(proprietorDirectorName);
             $('#proprietorDirectorContact-val').text(proprietorDirectorContact); 
             $('#local_contact_name-val').text(local_contact_name);
             $('#local_contact_no-val').text(local_contact_no);

            
             $('#gstin-val').text(gstin);
             $('#uin-val').text(uin);
             $('#pan-val').text(pan);
 
             $('#accountno-val').text(accountno);
             $('#accountname-val').text(accountname);
             $('#ifsc-val').text(ifsc);
             $('#bankname-val').text(bankname);
             $('#branch-val').text(branch);   
             $('#accounttype-val').text(accounttype);
             $('#insurno-val').text(insurno);
             $('#expirdate1-val').text(expirdate1);
             $('#expirdate2-val').text(expirdate2);
             $('#insurname-val').text(insurname);
             
                     
            $("#form-register").validate().settings.ignore = ":disabled,:hidden";
            return $("#form-register").valid();
               
        },
        onFinished: function (event, currentIndex) {

                   
            var form = $(this);
            jQuery("#wizard").submit();
            // Submit form input
            form.submit();
        }
    });

    
    
});


   

/*$('table').on('click', '#btdelete', function(e){
    alert("dele");
    $(this).closest('tr').remove()
 })

 $(document).ready(function () { 

    $('#backs').click(function(){
   var mySteps = $('#form-total').steps();
    
    steps_api = mySteps.data('plugin_Steps');


    steps_api.prev();
 });
});
*/


