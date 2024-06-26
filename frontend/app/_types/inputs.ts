export type TextInputType = {
  id: string
  placeholder: string
  value: string
  errors?: string[]
  label?: string
  required?: boolean
  type?: 'text' | 'password' | 'email'
}
