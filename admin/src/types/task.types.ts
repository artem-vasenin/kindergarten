export interface ITask {
  id: number;
  name: string;
  description: string;
  checked: boolean;
  user_id: number;
}

export interface ITaskCreate {
  name: string;
  description?: string;
  checked?: boolean;
  user_id?: number;
}

export interface ITaskUpdate {
  name?: string;
  description?: string;
  checked?: boolean;
  user_id?: number;
}
