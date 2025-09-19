import { z } from 'zod';
import { api } from '@/libs/api-client';
import { useMutation } from '@tanstack/react-query';
import type { MutationConfig } from '@/libs/react-query';

export const loginInputSchema = z.object({
  username: z.string().min(1, 'Required'),
  password: z.string().min(1, 'Required'),
});

export type LoginInput = z.infer<typeof loginInputSchema>;

export const loginApi = ({ data }: { data: LoginInput }): Promise<any> => {
  return api.post('/auth/login', data);
};

type UseLoginOptions = {
  mutationConfig?: MutationConfig<typeof loginApi>;
};

export const useLogin = ({ mutationConfig }: UseLoginOptions) => {
  const { onSuccess, ...restConfig } = mutationConfig || {};

  return useMutation({
    onSuccess: (...args) => {
      onSuccess?.(...args);
    },
    mutationFn: loginApi,
    ...restConfig,
  });
};
