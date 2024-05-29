'use client'

import { FormEvent, useState } from 'react'
import api from '@/app/_api/api'
import Form from '@/app/_components/form'
import { TextInputType } from '@/app/_types/inputs'
import { formDataToObj } from '@/app/_helpers/formDataToObj'

export default function Register() {
  const registerInputs: TextInputType[] = [
    {
      defaultValue: 'test',
      id: 'username',
      placeholder: 'Username',
    },
    {
      defaultValue: 'test@test.com',
      id: 'email',
      placeholder: 'Email',
      type: 'email',
    },
    {
      defaultValue: 'test',
      id: 'password',
      placeholder: 'Password',
      type: 'password',
    },
  ]
  const successMessage = 'Check your email to verify your account.'

  const [isLoading, setIsLoading] = useState<boolean>(false)
  const [apiFormErrors, setApiFormErrors] = useState<ApiResponseType | null>(null)
  const [formSuccess, setFormSuccess] = useState(false)

  async function handleSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault()
    setIsLoading(true)
    setApiFormErrors(null)

    const data = formDataToObj(event)

    try {
      await api.post('/auth/users', {
        ...data,
      })
      setIsLoading(false)
      setFormSuccess(true)
    } catch (error: any) {
      setIsLoading(false)
      const { response } = error
      setApiFormErrors(response)
    }
  }

  return (
    <>
      <h1>Register</h1>
      <Form
        buttonLabel='Register'
        inputsFields={registerInputs}
        inputsErrors={apiFormErrors}
        onSubmit={handleSubmit}
        successMessage={formSuccess ? successMessage : undefined}
      />
      {isLoading && <p>Loading...</p>}
    </>
  )
}
