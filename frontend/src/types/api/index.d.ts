export interface ApiResponse<T> {
  isError: boolean;
  message: string;
  data?: T;
  errors?: string[];
}
