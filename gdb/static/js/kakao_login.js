window.Kakao.init("d478f27c3f56914f0f62751b6b8534e6")

function kakaoLogin() {
    window.Kakao.Auth.login({
        scope:'profile_nickname, profile_image',
        success: function(authObj) {
            console.log(authObj);
            window.Kakao.API.request({
                url:'/v2/user/me',
                success: res => {
                    const kakao_account = res.kakao_account;
                    console.log(kakao_account);
                }
            })
        }
    });
}