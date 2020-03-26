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
                //remove default #finish button
                //$('.actions > ul > li:first-child').attr('style', 'display:none');
                $('.actions > ul > li:last-child').attr('style', 'display:none');
               // var $input = $('#backs');
               $('ul[aria-label=Pagination] button').remove();
                var $input = $('#subm');
                $input.appendTo($('ul[aria-label=Pagination]'));
                //$('a[href="#previous"]').appendTo($('#backs'));
                $input.attr('style', 'display:block');
              //$input.appendTo($('button'));


              // $('.actions > ul > li:last-child').attr('style', 'display:none');              
                 // $('ul[aria-label=Pagination] button').append();   
                 $('.actions > ul > li:last-child').attr('style', 'display:none');                            
                 $('a[href="#finish"]').remove();
                 $input.appendTo($('ul[aria-label=Pagination]'));       
                 $input.attr('style', 'display:block');
               }
               else {
               
                $('ul[aria-label=Pagination] input[value="Submit"]').remove();           
               }
              
        },

              
       onStepChanging: function (event, currentIndex, newIndex) { 

            var adddoor = $('#adddoor').val();
            var company_branch_name = $('#company_branch_name').val();
            var locality = $('#locality').val();
            var state = $('#state').val();
            var pincode = $('#pincode').val();
            var primary_contact_name = $('#primary_contact_name').val();
            var primary_contact_no= $('#primary_contact_no').val();
            var primary_email = $('#primary_email').val();
            var secondary_contact_name = $('#secondary_contact_name').val();
            var secondary_contact_no = $('#secondary_contact_no').val();
            var secondary_email = $('#secondary_email').val();
            var gstin= $('#gstin').val();
            var uin= $('#uin').val();
            var insurcompany= $('#insurcompany').val();
            var insurno= $('#insurno').val();
            var expirydate= $('#expirydate').val();


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
            var company_name = $('#company_name').val();

            var account_id = $('#account_id').val();
            var created_date = $('#created_date').val();
            var contact_person_name = $('#contact_person_name').val();
            var contact_no = $('#contact_no').val();

            var entity_name1 = $('#entity_name1').val();
            var entity_mail1 = $('#entity_name1').val();
            var entity_adddoor1 = $('#entity_adddoor1').val();
            var entity_locality1 = $('#entity_locality1').val();
            var entity_state1 = $('#entity_state1').val();
            var entity_pincode1 = $('#entity_pincode1').val();
            var entity_mobile_no1 = $('#entity_mobile_no1').val();
            var entity_gstin1 = $('#entity_gstin1').val();
            var entity_uin1= $('#entity_uin1').val();
            var entity_pan1 = $('#entity_pan1').val();
            var entity_insur_no1 = $('#entity_insur_no1').val();
            var entity_insur_name1 = $('#entity_insur_name1').val();
            var entity_expiry_date1 = $('#entity_expiry_date1').val();

            var entity_name2 = $('#entity_name2').val();
            var entity_mail2 = $('#entity_name2').val();
            var entity_adddoor2 = $('#entity_adddoor2').val();
            var entity_locality2 = $('#entity_locality2').val();
            var entity_state2 = $('#entity_state2').val();
            var entity_pincode2 = $('#entity_pincode2').val();
            var entity_mobile_no2 = $('#entity_mobile_no2').val();
            var entity_gstin2 = $('#entity_gstin2').val();
            var entity_uin2= $('#entity_uin2').val();
            var entity_pan2 = $('#entity_pan2').val();
            var entity_insur_no2 = $('#entity_insur_no2').val();
            var entity_insur_name2 = $('#entity_insur_name2').val();
            var entity_expiry_date2 = $('#entity_expiry_date2').val();

            var entity_name3 = $('#entity_name3').val();
            var entity_mail3 = $('#entity_name3').val();
            var entity_adddoor3 = $('#entity_adddoor3').val();
            var entity_locality3 = $('#entity_locality3').val();
            var entity_state3 = $('#entity_state3').val();
            var entity_pincode3 = $('#entity_pincode3').val();
            var entity_mobile_no3 = $('#entity_mobile_no3').val();
            var entity_gstin3 = $('#entity_gstin3').val();
            var entity_uin3= $('#entity_uin3').val();
            var entity_pan3 = $('#entity_pan3').val();
            var entity_insur_no3 = $('#entity_insur_no3').val();
            var entity_insur_name3 = $('#entity_insur_name3').val();
            var entity_expiry_date3 = $('#entity_expiry_date3').val();

              var account_id = $('#account_id').val();

             $('#companyBranchName-val').text(companyBranchName);
             $('#adddoor-val').text(adddoor);
             $('#locality-val').text(locality);
             $('#state-val').text(state);
             $('#pincode-val').text(pincode);
             $('#primary_contact_name-val').text(primary_contact_name);
             $('#primary_contact_no-val').text(primary_contact_no);
             $('#primary_email-val').text(primary_email);
             $('#secondary_contact_name-val').text(secondary_contact_name);
             $('#secondary_contact_no-val').text(secondary_contact_no);
             $('#secondary_email-val').text(secondary_email);
             $('#gstin-val').text(gstin);
             $('#uin-val').text(uin);
             $('#insurcompany-val').text(insurcompany);
             $('#insurno-val').text(insurno);
             $('#expirydate-val').text(expirydate);


             $('#account_id-val').text(account_id);
             $('#created_date-val').text(created_date);
             $('#contact_person_name-val').text(contact_person_name);
             $('#contact_no-val').text(contact_no);

              $('#entity_name1-val').text(entity_name1);
              $('#entity_mail1-val').text(entity_mail1);
              $('#entity_adddoor1-val').text(entity_adddoor1);
              $('#entity_locality1-val').text(entity_locality1);
               $('#entity_state1-val').text(entity_state1);
              $('#entiy_pincode1-val').text(entity_pincode1);
              $('#entiy_mobile_no1-val').text(entity_mobile_no1);
              $('#entity_gstin1-val').text(entity_gstin1);
              $('#entity_uin1-val').text(entity_uin1);
              $('#entity_pan1-val').text(entity_pan1);
              $('#entity_insur_name1-val').text(entity_insur_name1);
              $('#entity_insur_no1-val').text(entity_insur_no1);
              $('#entity_expiry_date1-val').text(entity_expiry_date1);

              $('#entity_name2-val').text(entity_name2);
              $('#entity_mail2-val').text(entity_mail2);
              $('#entity_adddoor2-val').text(entity_adddoor2);
              $('#entity_locality2-val').text(entity_locality2);
              $('#entity_state2-val').text(entity_state2);
              $('#entiy_pincode2-val').text(entity_pincode2);
              $('#entiy_mobile_no2-val').text(entity_mobile_no2);
              $('#entity_gstin2-val').text(entity_gstin2);
              $('#entity_uin2-val').text(entity_uin2);
              $('#entity_pan2-val').text(entity_pan2);
              $('#entity_insur_name2-val').text(entity_insur_name2);
              $('#entity_insur_no2-val').text(entity_insur_no2);
              $('#entity_expiry_date2-val').text(entity_expiry_date2);

              $('#entity_name3-val').text(entity_name3);
              $('#entity_mail3-val').text(entity_mail3);
              $('#entity_adddoor3-val').text(entity_adddoor3);
              $('#entity_locality3-val').text(entity_locality3);
              $('#entity_state3-val').text(entity_state3);
              $('#entiy_pincode3-val').text(entity_pincode3);
              $('#entiy_mobile_no3-val').text(entity_mobile_no3);
              $('#entity_gstin3-val').text(entity_gstin3);
              $('#entity_uin3-val').text(entity_uin3);
              $('#entity_pan3-val').text(entity_pan3);

              $('#entity_insur_name3-val').text(entity_insur_name3);
              $('#entity_insur_no3-val').text(entity_insur_no3);
              $('#entity_expiry_date3-val').text(entity_expiry_date3);
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


