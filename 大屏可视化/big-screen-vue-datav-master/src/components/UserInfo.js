import React from 'react';

const UserInfo = ({ user, onLogout }) => {
  return (
    <div className="user-info">
      <span>当前登录用户: {user.name}</span>
      <button onClick={onLogout}>退出</button>
    </div>
  );
};

export default UserInfo;