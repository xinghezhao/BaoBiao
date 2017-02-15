function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var USERNAME = '';
$('document').ready(function(){


	$('#login_submit').click(function(){
	    var csrftoken = getCookie('csrftoken');
	    var username = $('#username').val();
	    var password = $('#password').val();

		$.ajax({
		    cache: false,
			type: "POST",
            url: "/signin/",
            dataType:'json',
            async: true,
			data:{
				username: username, //用户名
				password: password  //密码
			},
			success: function(data) {
				 if (data.status == 'fail') {
						alert('用户名或密码错误')
				 }
				 if (data.status == 'fail1') {
					 alert('用户名必填并且密码必须要五位以上')
				 }
				 if(data.status == 'success') {
					 window.location.href = "/index";
				 }


			},
            beforeSend: function(xhr, settings) {
              xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
		});
	});





	//选择时间开始
	var t_start = null;
	var t_end = null

	laydate({
	  elem: '#start_time', //目标元素。由于laydate.js封装了一个轻量级的选择器引擎，因此elem还允许你传入class、tag但必须按照这种方式 '#id .class'
	  event: 'focus', //响应事件。如果没有传入event，则按照默认的click
	  format: 'YYYY-MM-DD hh:mm:ss', //
	  // max: laydate.now(), //设定最大日期为当前日期
	  istime: true,
	  istoday: false, //是否显示今天

	  choose: function(datas){ //选择日期完毕的回调
		    var timestamp = Date.parse(datas);
			t_start = (timestamp / 1000)-8*60*60;
		}
	});


	laydate.skin('molv')
	laydate({
	  elem: '#end_time', //目标元素。由于laydate.js封装了一个轻量级的选择器引擎，
	  					//因此elem还允许你传入class、tag但必须按照这种方式 '#id .class'
	  event: 'focus', //响应事件。如果没有传入event，则按照默认的click
	  format: 'YYYY-MM-DD hh:mm:ss', //
	  max: laydate.now(), //设定最大日期为当前日期
	  istime: true,
	  istoday: false, //是否显示今天
	  choose: function(datas){ //选择日期完毕的回调
		    var timestamp = Date.parse(datas);
			t_end = (timestamp / 1000)-8*60*60;
		}
	});
	// 选择时间end
});






