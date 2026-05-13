export enum RoleType {
  ADMIN = 'admin',
  GUEST = 'guest',
}

export interface IProfile {
  id: number;
  email: string;
  role: RoleType;
}

export interface IRegister {
  email: string;
  password: string;
  role?: RoleType;
}

export interface ILogin {
  email: string;
  password: string;
}

export interface IProfileUpdate {
  password?: string;
  role?: RoleType;
}
