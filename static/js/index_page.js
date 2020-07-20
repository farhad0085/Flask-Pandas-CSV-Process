$(document).ready(function() {

    $("#select_first").on('click', function() {

        $("#file_first").click();

    });
    $("#select_second").on('click', function() {

        $("#file_second").click();

    });
    $("#select_third").on('click', function() {

        $("#file_third").click();

    });


    $("#file_first").change(function(event) {

        $("#file_upload_1").show();
        $("#filename_1").text(event.target.files[0].name.slice(0,25));
        $("#filesize_div_1").text((event.target.files[0].size/(1000*1000)).toFixed(2) + " MB");

    });

    $("#file_second").change(function() {

        $("#file_upload_2").show();
        $("#filename_2").text(event.target.files[0].name.slice(0,25));
        $("#filesize_div_2").text((event.target.files[0].size/(1000*1000)).toFixed(2) + " MB");

    });

    $("#file_third").change(function() {

        $("#file_upload_3").show();
        $("#filename_3").text(event.target.files[0].name.slice(0,25));
        $("#filesize_div_3").text((event.target.files[0].size/(1000*1000)).toFixed(2) + " MB");

    });


    // form submit

    $('form').on('submit', function(event) {
        $("#file_downloads").hide();
        $("#drive_links").attr('style', 'display: none !important');

        event.preventDefault();

        if($("#file_third").get(0).files.length === 0 || $("#file_second").get(0).files.length === 0 || $("#file_first").get(0).files.length === 0){

            swal({
                      title: "Attention!",
                      text: "Please upload all three files!",
                      icon: "warning",
                      button: "Okay",
                    })
           return false;
        }

        var formData = new FormData($('form')[0]);

        $.ajax({
            xhr: function() {
                var xhr = new window.XMLHttpRequest();

                xhr.upload.addEventListener('progress', function(e) {

                    console.log(e);

                    if (e.lengthComputable) {

                        console.log('Bytes Loaded: ' + e.loaded);
                        console.log('Total Size: ' + e.total);
                        console.log('Percentage Uploaded: ' + (e.loaded / e.total))

                        var percent = Math.round((e.loaded / e.total) * 100);

                        $('#progressDiv').show();
                        $('#progressBar').css('width', percent + '%');
                        $('#submitButton').val("Uploading ...");

                        if(percent==100){
                            $('#submitButton').val("File Uploaded");
                            $("#loading_spinner").show();
                            $("#loading_msg").show();
                            $('html, body').animate({
                                    scrollTop: $("#loading_spinner").offset().top
                                }, 2000);
                        }
                    }

                });

                return xhr;
            },
            type: 'POST',
            url: '/',
            data: formData,
            processData: false,
            contentType: false,
            success: function(responseData) {
                $('#submitButton').val("Upload");
                $('#progressBar').css('width', '0%');
                $('#progressDiv').hide();
                swal({
                      title: "Success!",
                      text: "Processing Completed, Now you can download your files!",
                      icon: "success",
                      button: "Okay",
                    }).then(function() {
                            $("#loading_spinner").hide();
                            $("#loading_msg").hide();

                            // set received file infos
                            $("#drive_link_1").attr('href', "https://drive.google.com/open?id="+responseData.drive_links[0])
                            $("#drive_link_2").attr('href', "https://drive.google.com/open?id="+responseData.drive_links[1])
                            $("#drive_link_1").text("https://drive.google.com/open?id="+responseData.drive_links[0])
                            $("#drive_link_2").text("https://drive.google.com/open?id="+responseData.drive_links[1])
                            $("#drive_links").show()

                            $("#filename_1_down").text(responseData.filenames[0])
                            $("#filename_2_down").text(responseData.filenames[1])
                            $("#filesize_div_1_down").text(responseData.filesize[0])
                            $("#filesize_div_2_down").text(responseData.filesize[1])
                            $("#download_link_1").attr('href', responseData.filelinks[0])
                            $("#download_link_2").attr('href', responseData.filelinks[1])

                            $("#file_downloads").show();
                            $('html, body').animate({
                                    scrollTop: $("#file_downloads").offset().top
                                }, 2000);
                        });
            },
            error: function(XMLHttpRequest, textStatus, errorThrown) { 
		        $('#submitButton').val("Upload");
                $('#progressBar').css('width', '0%');
                $('#progressDiv').hide();
                swal({
                      title: "Failed!",
                      text: "Error: Please double check that either you have uploaded right csv or use right sequence!",
                      icon: "error",
                      button: "Okay",
                    }).then(function() {
                            $("#loading_spinner").hide();
                            $("#loading_msg").hide();
                        });
		    }  
        });

    });

});