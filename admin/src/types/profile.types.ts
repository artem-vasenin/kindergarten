export enum RoleType {
  ADMIN = 'admin',
  GUEST = 'guest',
}

export interface IProfile {
  id: number;
  email: string;
  role: RoleType;
}

export interface ILogin {
  email: string;
  password: string;
}
