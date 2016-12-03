$(window).load(function() {
    //Declare the speech object & set attributes
    utterance = new window.SpeechSynthesisUtterance();
    utterance.lang = 'en-US';
    utterance.volume = 1.0;
    utterance.rate = 1.0;
    utterance.pitch = 1.0;
    
        //Speak the phrase
    window.speechSynthesis.speak(utterance);
    window.speechSynthesis.onvoiceschanged = function () {
        console.log("voice changed")
        var voices = speechSynthesis.getVoices();
        utterance.voice = voices.filter(function(voice) { return voice.name == 'Google UK English Female'; })[0];
    };
    window.speechSynthesis.speak(utterance);
});


  PingherUtil={
		  startDictation : function(){
			  if (window.hasOwnProperty('webkitSpeechRecognition')) {
			      //var snd = new Audio("/static/pingherapp/assets/sounds/ahhh.wav");
			      var snd = new Audio("/static/pingherapp/assets/sounds/beep.wav");   
			      snd.play(); 
			      var recognition = new webkitSpeechRecognition();
			      recognition.continuous = false;
			      recognition.interimResults = false;
			      recognition.lang = "en-US";
			      recognition.start();
			      //if ('speechSynthesis' in window) {
         //                        voices = window.speechSynthesis.getVoices();
         //                        VoiceMsg.voice = voices.filter(function(voice) { return voice.name == 'Google UK English Female'; })[0];
         //                        console.log(VoiceMsg);       
         //                     }
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
			            var d = new Date();
			            var parentList=$("ul.chats");
			            var answerUI="<li class='out'><img class='avatar' alt='' src='/static/pingherapp/assets/layouts/layout/img/avatar2.jpg' /><div class='message'><span class='arrow'> </span><a href='javascript:;' class='name'> Her </a><span class='datetime'> at "+d.getHours()+":"+d.getMinutes()+"</span><span class='body'>"+result+"</span></div></li>"
			            parentList.append(answerUI);
			            if ('speechSynthesis' in window) {
			                utterance.text = result;
                                        window.speechSynthesis.speak(utterance);
			            }
			            
			   
                                
			        }});
			        
			      };
			  
			      recognition.onerror = function(e) {
			        recognition.stop();
			      }
			 
			    }   
			}
	}