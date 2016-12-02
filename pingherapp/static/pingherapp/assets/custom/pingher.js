  PingherUtil={
		  startDictation : function(){
			  if (window.hasOwnProperty('webkitSpeechRecognition')) {
				  
			      var recognition = new webkitSpeechRecognition();
			      recognition.continuous = false;
			      recognition.interimResults = false;
			      recognition.lang = "en-US";
			      recognition.start();

			      recognition.onresult = function(e) {
    			      
			      document.getElementById('transcript').value
			                                 = e.results[0][0].transcript;
			        recognition.stop();
			      var d = new Date();
			      var question=$("input[name='q']").val();
			      var questionUI="<li class='in'><img class='avatar' alt='' src='/static/pingherapp/assets/layouts/layout/img/avatar1.jpg' /><div class='message'><span class='arrow'> </span><a href='javascript:;' class='name'> You </a><span class='datetime'> at "+d.getHours()+":"+d.getMinutes()+" </span><span class='body'>"+question+"</span></div></li>"
    			      var parentList=$("ul.chats");
    			      parentList.append(questionUI);
			        //document.getElementById('labnol').submit();
			        data={question:question}
			        $.ajax({
			        	url: "askQuestion", 
			        	data: data,
			        	success: function(result){
			            console.log(result);
			        }});
			        
			      };
			  
			      recognition.onerror = function(e) {
			        recognition.stop();
			      }
			 
			    }   
			}
	}